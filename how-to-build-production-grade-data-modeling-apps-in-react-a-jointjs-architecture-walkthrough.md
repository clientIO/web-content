---
source: https://www.jointjs.com/blog/how-to-build-production-grade-data-modeling-apps-in-react-a-jointjs-architecture-walkthrough
generated: 2026-10-09
format: markdown
---

If you’re building data modeling UIs like ERD editors, data lineage views, or similar, the diagram looks like the easy half of the project. You just need to build boxes that list rows, links between the boxes, an export button at the end, and you're done. But that really is the easy part. The hard part is the structure and rules underneath.

Those requirements are not just related to UI. A relation doesn't simply connect two tables, but rather connects one column to another, and it has to stay anchored to that column while the table is dragged, resized, or has new rows inserted above it. A column pair can carry at most one foreign key, in either direction, so drawing the reverse of an existing relation needs to be rejected rather than duplicated. Deleting a column has to delete the relations anchored on it, and the generated SQL in the side panel has to be correct, dialect-aware, and current, without regenerating sixty times a second while someone drags a table across the paper.

In reality, this is a modeling problem with a diagram on top, and that’s where most of the development time, effort, and tokens go in any of these apps.

We built a proper data modeling app as a demo to show how you can build something like this with JointJS+ for React, or better yet, so you can take it as a starting point for your own data modeling application. In this article, you’ll get a short overview of some patterns used to develop the app.

## **About JointJS+ Data Modeling demo**

[Data Modeling Demo in JointJS+ for React](https://www.jointjs.com/demos/data-modeling) is a database schema designer. It lets users design database schemas visually. It features everything a serious data-modeling app must have, from tables with typed columns, keys, nullability, defaults, to indexes, all editable inline or through an inspector. Users can easily create foreign keys by dragging links from one column to another, tables can be organized into collapsible groups so a hundred-table schema stays navigable, and much more.

What makes it more than a picture is the SQL. The schema compiles to DDL (CREATE TABLE, CREATE INDEX, and the other structural statements) and runs against a real database engine in the browser: SQLite through sql.js, PostgreSQL through PGlite, with a query panel on top. You can also paste in an existing SQL and watch the diagram rebuild itself from it.

You can easily install and test it through [@joint/cli tool](https://www.npmjs.com/package/@joint/cli):

```
npx @joint/cli download data-modeling/react
```

You will need access to the JointJS+ for React package, through a license or a [free trial](https://www.jointjs.com/free-trial). The full source code is available on GitHub:<https://github.com/clientIO/joint-demos/tree/main/data-modeling>

## **The graph carries the schema**

The decision that determines everything isn’t about rendering, but that there should be one source of truth, which is the graph itself. Every cell in the diagram carries a typed data payload with a `kind` property specifying the cell type:

```
// src/model/cell-data.ts

export interface TableCellData {
   readonly kind: 'table';
   readonly table: Table;
   // Optional background tint preset. Presentation only — not part of the SQL model.
   readonly fill?: SwatchKey;
}
```

The `Table`, with its columns, types, and keys, lives on the cell, and there’s no second schema object that needs to be kept in sync. The diagram is in [Controlled Mode](https://docs.jointjs.com/react/data-management/controlled-mode/) (`<Diagram cells>`), so `cells` is React state, and every edit flows back through `setCells`.

The graph is a plain serializable structure, so you can convert between it and the schema with two functions:

```
// src/model/schema-cells.ts

export function schemaToCells(schema: Schema, notes: readonly NoteSeed[] = []): Cell[]
export function cellsToSchema(cells: readonly Cell[]): Schema
```

The `schemaToCells` function turns a schema into something the canvas can draw, while the `cellsToSchema` reads the schema back from the canvas.

That’s precisely what lets us keep the separation of concerns and avoid mixing SQL with diagramming logic. The `schema/` and `db/` folders hold 2,532 lines of TypeScript (including tests): DDL generation, SQL parsing, dialect type mapping, and both database engine adapters. None of it imports JointJS, so the parts that are hardest to get right, generating correct DDL and parsing someone else's SQL file, can easily be unit-tested.

## **Tables are components**

A table card needs a header you can rename inline, a row per column with a type dropdown, key icons, nullable and unique markers, an index marker, and a delete button. With most diagramming libraries, you have to define every detail of the table card using shape markup and then manually arrange each part. As a result, you end up building your own layout engine.

In this app, with JointJS, the card is a React component, and the paper decides which component to render based on the kind property on the cell's data:

```
// src/canvas/render-element.tsx

export const renderElement: RenderElement<ElementCellData> = (data) => {
   if (isTableCell(data)) return <TableCard table={data.table} />;
   if (isGroupCell(data)) return <GroupElement />;
   if (isNoteCell(data)) return <NoteCard />;
   return null;
};
```

That's the whole file apart from imports. `TableCard` is rendered as an `<HTMLBox>`, a JointJS wrapper that keeps a block of real HTML aligned with its element on the canvas, and `useModelGeometry` tells it to take its width and height from that element. Inside the box, you're writing ordinary markup like Tailwind classes, Radix dropdowns, focus rings, and a scrollable list of columns.

Edits back into the cell are handled with one function:

```
// src/canvas/table-edit.ts

export function updateTable(api: TableGraph, id: CellId, map: (table: Table) => Table): void {
   api.setCell(id, (previous) => {
       if (!api.isElement(previous)) return previous;
       const { data } = previous;
       if (!isTableCell(data)) return previous;
       return { ...previous, data: { ...data, table: map(data.table) }};
   });
}
```

`setCell` takes a function rather than a value, so it always runs against the current cell, and never a stale copy, and the two guards confirm you're holding a table first. Renaming a column, changing its type, toggling NOT NULL, just passes a different updater.

Columns that aren’t changed return as the same objects, and the rows are memoized, so React re-renders only the one you edited.

## **Connections that land on columns**

Most diagramming libraries connect nodes, but in data modeling, links happen between fields, which can be a massive challenge for many libraries.

JointJS handles this with magnets. Every column row is a magnet with an id derived from the column (`columnMagnet(col.id)`):

```
// src/model/schema-cells.ts

function relationCell(relation: Relation): Cell {
   return {
       id: relation.id,
       type: 'link',
       source: { id: relation.source.tableId, magnet: columnMagnet(relation.source.columnId) },
       target: { id: relation.target.tableId, magnet: columnMagnet(relation.target.columnId) },
       data: {
           kind: 'relation',
           relationId: relation.id,
           cardinality: relation.cardinality,
           onDelete: relation.onDelete,
           onUpdate: relation.onUpdate,
       },
   };
}
```

An endpoint stores a table id and a magnet id, never a position. Reading the schema back out is then a matter of turning `col-<id>` into a column id again, which is what `cellsToSchema` does. And because the line is attached to the column rather than to a point in space, you can drag the table, resize it, or insert any number of rows above that column, and the foreign key will still point where it did.

Which connections are permitted is in configuration, not validation code you would have to write. The object `VALIDATE_CONNECTION` is set directly as a paper prop, `<Paper validateConnection={…}>`:

```
// src/canvas/canvas.tsx

const VALIDATE_CONNECTION: NonNullable<PaperProps['validateConnection']> = {
   allowRootConnection: false,
   linkLimit: 'one-per-pair',
};
```

Setting `allowRootConnection: false` rejects links dropped on the table body, and `linkLimit: 'one-per-pair'` allows a single link between any two columns, in either direction.

## **Live SQL that doesn’t fire on every frame**

The SQL panel doesn’t keep a copy of the schema. It reads the cells and generates the DDL as it renders. As dragging a table commits a new array around sixty times a second, and regenerating SQL on every frame isn't an option, we use the second argument of `useCells`:

```
// src/model/use-schema.ts

export function useSchema(): Schema {
   return useCells(cellsToSchema, schemasEqual);
}
```

`useCells` takes a selector and a comparison. It runs `cellsToSchema` when the cells change, compares the result to the previous one, and if they’re the same, nothing is re-rendered. Position isn't part of a schema, so a drag produces an equal result and no SQL is generated.

That comparison runs on every commit, so it has to be inexpensive. Tables and groups are compared by reference, which works because edits are immutable (editing a table creates a new object, moving one doesn't). Relations are rebuilt each time, so those are compared field by field.

The SQL panel works in reverse too. Edit the DDL and hit Apply, and the parsed schema is merged into the cells rather than replacing them, since SQL has no way to express groups, notes, or layout.

## **Keyboard and screen reader access**

Diagramming apps tend to skip accessibility on the grounds that diagrams are mainly visual tools. A serious application wouldn’t use this as an excuse, which is precisely why we paid special attention to getting the Data Modeling app template as accessible as possible.

From ensuring sufficient contrast in both light and dark modes, to making sure everything in the app can be handled purely with the keyboard (yes, even adding nodes, links, and moving elements around), to the basics of defining proper roles for the nodes, with correct labels.

```
// src/canvas/table-card.tsx

<div
   role="application"
   aria-roledescription="diagram node"
   aria-label={`Table ${table.name}`}
>
```

On top of that, users need to understand what’s actually happening in the app, which is why there are clearly defined ARIA live regions (invisible hooks that tell screen readers to announce dynamic content updates without moving the user's keyboard focus).

Getting accessibility right is very challenging, which is precisely why we did the heavy lifting for you and set up the Data Modeling app accessibility structure you can easily build from.

## **Groups, collapse, and scale**

The tables in the app live in collapsible group containers. The hook that handles this calculates group members when a table is dragged, a group is resized, or when something is added to a group, but deliberately not while a group is being *moved*, so a group sliding across the paper doesn’t randomly pick up tables when it passes over them.

Collapsing a group to its header is an ordinary edit through the controlled cells, since calling `element.resize()` directly would be undone on the next render. Hiding its contents is a function you give to `<Paper cellVisibility>`, which decides whether a cell should be rendered.

The app is built for performance and large schemas. Most notably, `virtualRendering` renders only the cells in view, and `spatialIndex` puts hit-testing and containment checks behind a quad-tree. Check out our [in-depth guide on JointJS performance](https://www.jointjs.com/blog/10-practical-jointjs-performance-tips-for-fast-efficient-production-grade-diagrams) if you want to learn more about the techniques used to make this app silky-smooth at production-grade scale.

## **What you get out of the box with JointJS+**

The entire interaction layer of this app is a handful of props on <Diagram>, the JointJS+ root component:

```
// src/app.tsx

<Diagram
   cells={cells}
   onCellsChange={handleCellsChange}
   history
   clipboard
   spatialIndex
   interactions={{ paperScroller: armed === null, commandManager: false }}
>
```

Place `<Selection>` and `<Snaplines>` inside the paper, with a minimap in the corner, and you get undo and redo, copy and paste, marquee selection, and alignment guides while you drag. As they’re part of the library, they’re maintained for you and work flawlessly in sync.

## **Adapting the Data Modeling app to your own domain**

Hardly any of the code outlined here is specific to SQL. The diagramming and schema logic are separated; links are connecting fields and node boxes, so if you replace tables and columns with your own model, whether that's a semantic layer editor, a tool for mapping one set of fields onto another, a lineage view, or a migration planner,  everything will work precisely as expected.

Plenty of libraries can draw boxes and connect lines. The difference with JointJS is that there's a real model underneath, where design, rules, accessibility, and usability are critical, and the interaction layer with editing features your users expect is already built in.

## **Getting started**

The easiest way to get started with the Data Modeling application is to install it locally and ask your AI coding agent to tweak it precisely towards your use case:

```
npx @joint/cli download data-modeling/react
```

The source is heavily commented with the reasoning behind each decision. Those comments are also why the codebase works well with an AI coding agent. For best results, set up the [JointJS MCP Server](https://docs.jointjs.com/learn/help-center/mcp-server/), which has direct access to up-to-date JointJS docs and all high-quality demo application code.

- Learn more about Data Modeling with JointJS
- [See the Data Modeling demo in action](https://www.jointjs.com/demos/data-modeling)
- Check JointJS for React docs
- Start your free JointJS+ trial

Happy diagramming!

‍

## FAQ

What is the Data Modeling app template built with?

Do I need a JointJS+ license to use the demo?

Can I import and export SQL schemas?

How does the app handle schema logic?

Is the app accessible?

Is the codebase adaptable for other domains?

How do I get started with the template?