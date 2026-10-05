---
source: https://www.jointjs.com/blog/jointjs-for-react-key-differences-that-change-how-you-build-production-grade-diagrams
generated: 2026-10-05
format: markdown
---

JointJS for React ([@joint/react](https://www.npmjs.com/package/@joint/react)) is a native React integration for JointJS. It makes adding production-grade diagrams to React applications much easier.

If you’ve embedded JointJS into a React app before, you already know that you have to jump through hoops with a useEffect wrapper, create a graph and paper imperatively, attach and remove event listeners by hand, and keep React state in sync through custom bridge code. It works, but it’s not elegant, and it's not how you’d expect it to work in the React ecosystem.

JointJS for React fixes all of that and makes JointJS work with React natively. Diagram cells become React-readable state, nodes are plain React components, and setup, cleanup, events, and data flow follow familiar React patterns.

In this guide, you’ll see eight common integration patterns side by side, with code examples showing how you’d handle each one before, by integrating JointJS into React manually, and how you handle it now with the native JointJS for React integration.

**Note about JointJS and JointJS for React**

JointJS for React is a native React integration for JointJS. The JointJS core library is still actively developed, it’s used by JointJS for React, and it’s the right choice for vanilla JavaScript and other frameworks.

The [@joint/core](https://www.npmjs.com/package/@joint/core) is deliberately low-level, so you can configure everything through its API. JointJS for React adds a layer of convenience on top with related options combined into single choices, sensible defaults, callbacks that receive named values instead of positional arguments, and styling that looks great out of the box.

In [Introducing JointJS for React](https://www.jointjs.com/blog/introducing-jointjs-for-react), we compared a basic *Hello World* setup before and after. This guide goes further and covers what changes across a real component: state, rendering, events, sizing, data flow, and types.

## **1. Basic diagram setup**

With a manual integration, you have to repeat the same lifecycle code in every component that hosts a diagram, from refs for the graph and the paper, a `useEffect` that constructs them against a DOM node, to a cleanup callback.

**Before: manual integration**

```
// DO NOT USE - Old way of integrating JointJS with React

import { useEffect, useRef } from 'react';
import { dia, shapes } from '@joint/core';

const cellNamespace = shapes;

function Diagram() {
  const containerRef = useRef <HTMLDivElement> null;

  // Kept in refs so handlers, other effects, and child components can reach them
  const graphRef = (useRef <dia.Graph) | (null> null);
  const paperRef = (useRef <dia.Paper) | (null> null);

  useEffect(() => {
    const container = containerRef.current;
    if (!container) return;

    const graph = new dia.Graph({}, { cellNamespace });
    const paper = new dia.Paper({
      model: graph,
      cellViewNamespace: cellNamespace,
    });

    // Append instead of passing `el`, so paper.remove()
    // doesn't remove the React-owned <div> from the DOM
    container.appendChild(paper.el);

    graphRef.current = graph;
    paperRef.current = paper;

    return () => {
      paper.remove();
      graphRef.current = null;
      paperRef.current = null;
    };
  }, []);

  return <div ref={containerRef} />;
}
```

In production-grade apps, this setup usually evolves into a custom context provider that exposes the graph and paper to the rest of the tree, which is exactly what `GraphProvider` gives you.

**After: JointJS for React**

```
// New native JointJS for React integration

import { GraphProvider, Paper } from '@joint/react';

function Diagram() {
  return (
    <GraphProvider>
      <Paper style={{ width: '100%', height: '100%' }} />
    </GraphProvider>
  );
}
```

`<GraphProvider>` and `<Paper>` manage the lifecycle, and cleanup happens automatically when they unmount. There are no refs to manage and no mount effect to get wrong under double `useEffect` calls in React Strict Mode.

You also don't need a `cellNamespace` unless you register custom shapes, because the provider already includes the built-in ones, and you can size `<Paper>` with CSS instead of using `width` and `height` options.

## **2. Reading diagram state**

Before, reading a value out of the diagram meant subscribing to graph events inside a `useEffect`, filtering for the change you care about, and calling `setState`.

**Before: manual integration**

```
// DO NOT USE - Old way of integrating JointJS with React

const [label, setLabel] = useState('');

useEffect(() => {
  const graph = graphRef.current;
  if (!graph) return;

  // Read the initial value, or the label stays empty until the first change
  setLabel(graph.getCell(id)?.attr('label/text') ?? '');

  const handler = (cell: dia.Cell) => {
    if (cell.id === id) setLabel(cell.attr('label/text'));
  };
  graph.on('change:attrs', handler);
  return () => {
    graph.off('change:attrs', handler);
  };
}, [id]);
```

**After: JointJS for React**

```
// New JointJS for React native integration

const { label } = useCell(id, selectElementData);

const count = useCells((cells) => cells.length);
```

The manual version is convoluted, complex, and has plenty of pieces that can go wrong. You need to pick up the right event (`change:attrs`, not the catch-all change), write the id filter, and remember to read the initial value.

In JointJS for React, `useCell` and `useCells` return the current value on the first render and re-render only when the selected slice changes, so dragging a node never re-renders a component that only reads labels, and there’s no event name to get right.

The library provides selectors you can use to access state: `selectElementPosition`, `selectElementSize`, `selectElementAngle`, `selectElementData`, and `selectCellType`.

If you need raw JointJS events anyway, you can use `useOnGraphEvents` to listen for native events, such as add, remove, or `change:position`.

## **3. Rendering nodes as React components**

Before JointJS for React, a node’s appearance lived in a model class with SVG markup, attrs, and presentation logic in `defaults()`. It’s a powerful system, but in a React app it meant switching mental models, as CSS animations, a charting library inside a node, or content driven by app state all needed workarounds.

**Before: manual integration**

```
// DO NOT USE - Old way of integrating JointJS with React

class Node extends dia.Element {
  defaults() {
    return {
      ...super.defaults,
      type: 'Node',
      size: { width: 160, height: 60 },
      attrs: {
        body: { width: 'calc(w)', height: 'calc(h)', fill: '#1B2538', stroke: '#4D9FFF', rx: 6 },
        label: {
          x: 'calc(0.5*w)',
          y: 'calc(0.5*h)',
          text: '',
          fill: '#CAD3E5',
          textVerticalAnchor: 'middle',
          textAnchor: 'middle',
        },
      },
      markup: [
        { tagName: 'rect', selector: 'body' },
        { tagName: 'text', selector: 'label' },
      ],
    };
  }
}

// Register the shape so the graph and paper can resolve type: 'Node'
const cellNamespace = { ...shapes, Node };
```

**After: JointJS for React**

```
// New native JointJS for React integration

<Paper
  renderElement={({ label, status }) => (
    <HTMLHost>
      <div className={`node node--${status}`}>{label}</div>
    </HTMLHost>
  )}
/>
```

The `renderElement` prop accepts a plain React component, so you can use any hook, library, or stylesheet you’d use anywhere else in your app.

You also don’t need to hand-roll a `foreignObject`. HTMLHost renders the element as a `<div>` that sizes itself to its content and syncs the measured size back to the graph automatically. Because it sets its own width and height inline, style and size the content you put inside it rather than the host itself.

`HTMLBox` does the same with a default theme driven by `--jj-box-*` CSS variables; import `@joint/react/styles.css` and your nodes look right before you write any CSS.

## **4. Handling paper events without stale closures**

Before JointJS for React, setting up a paper listener in a component created the classic stale closure problem, so you had to re-subscribe on every change or maintain a ref by hand.

```
// DO NOT USE - Old way of integrating JointJS with React

// Keep the latest handler in a ref
const onSelectRef = useRef(onSelect);
useEffect(() => {
  onSelectRef.current = onSelect;
}, [onSelect]);

useEffect(() => {
  // Capture the paper locally
  const paper = paperRef.current;
  if (!paper) return;

  const handler = (view: dia.ElementView) => onSelectRef.current(view.model.id);
  paper.on('element:pointerclick', handler);
  return () => {
    paper.off('element:pointerclick', handler);
  };
}, []);
```

‍**After: JointJS for React**

```
// New native JointJS for React integration

<Paper onElementPointerClick={({ id }) => onSelect(id)} />
```

You only need to set up a prop on paper, precisely as it should be. The paper subscribes once and reads the current handler on every event, so you can use inline arrow functions, and you don’t need to wrap the parent's handler in `useCallback`.

You can also listen for paper events outside `<Paper>` with the `useOnPaperEvents` hook:

```
// New JointJS for React native integration

useOnPaperEvents({
  onElementPointerClick: ({ id }) => onSelect(id),
});
```

Handlers like `onElementPointerClick` get a single params object with named properties, instead of native JointJS event names with positional arguments. If you prefer JointJS core event names and arguments, such as `element:pointerclick`, you can use those in the same hook.

## **5. Auto-sizing nodes from measured content**

Before, a node that sized itself to HTML content meant writing a custom element view where you had to observe the HTML inside a `foreignObject`, write its size back to the model, and disconnect the observer when the view is removed.

**Before: manual integration**

```
// DO NOT USE - Old way of integrating JointJS with React

// The Card model's markup (not shown) has a <foreignObject> with a 'content' <div>
class CardView extends dia.ElementView {
  private observer: ResizeObserver | null = null;

  render() {
    super.render();
    this.observer?.disconnect();
    const content = this.findNode('content') as HTMLElement;
    this.observer = new ResizeObserver(([entry]) => {
      const [box] = entry.borderBoxSize;
      this.model.resize(Math.ceil(box.inlineSize), Math.ceil(box.blockSize));
    });
    this.observer.observe(content);
    return this;
  }

  onRemove() {
    this.observer?.disconnect();
    super.onRemove();
  }
}

const cellNamespace = { ...shapes, Card, CardView };
```

**After: JointJS for React**

```
// New native JointJS for React integration

<Paper
  renderElement={({ title }) => (
    <HTMLHost>
      <div className="card">{title}</div>
    </HTMLHost>
  )}
/>
```

`HTMLHost` measures its content, writes the size to the model, and cleans up with the element, so there's nothing to manage.

If you need your own markup around the HTML, such as an SVG shape behind it, you can use the `useMeasureElement` hook.

You can find more details about useMeasureElement in the [JointJS docs](https://docs.jointjs.com/api-react/Hooks/useMeasureElement/), and you can also check the [Resizable Node Example demo](https://react.jointjs.com/learn/?path=/docs/examples-resizable-node--docs&globals=backgrounds.grid:!true).

## **6. Syncing graph state with React**

Before, the graph owned its cell data, so to connect a diagram state to Redux or a parent `useState` you needed to listen for mutation events by hand, design the bridge and its contract yourself.

**Before: manual integration**

```
// DO NOT USE - Old way of integrating JointJS with React

const [cells, setCells] = useState<dia.Cell.JSON[]>(initialCells);
const fromGraphRef = useRef<dia.Cell.JSON[] | null>(null);
const applyingRef = useRef(false);

// Graph -> React
useEffect(() => {
 const graph = graphRef.current;
 if (!graph) return;
 const sync = () => {
   if (applyingRef.current) return; // ignore our own writes
   const next = graph.toJSON().cells;
   fromGraphRef.current = next;
   setCells(next);
 };
 graph.on('add remove change reset', sync);
 return () => { graph.off('add remove change reset', sync); };
}, []);

// React -> Graph
useEffect(() => {
 const graph = graphRef.current;
 if (!graph || cells === fromGraphRef.current) return; // change came from the graph
 applyingRef.current = true;
 graph.resetCells(cells); // rebuilds every view
 applyingRef.current = false;
}, [cells]);
```

**After: JointJS for React**

There are three modes, and each one is a prop.

**Uncontrolled:** JointJS owns the data after mount.

```
// New native JointJS for React integration

<GraphProvider initialCells={initialCells}>
  <Paper />
</GraphProvider>
```

**Controlled:** React drives the cells array, just like `<input value>`.

```
// New native JointJS for React integration

const [cells, setCells] = useState(initialCells);

<GraphProvider cells={cells} onCellsChange={setCells}>
  <Paper />
</GraphProvider>
```

**Incremental:** granular deltas per commit, ready for an external store.

```
// New native JointJS for React integration

<GraphProvider
  initialCells={initialCells}
  onIncrementalCellsChange={({ added, changed, removed }) =>
    store.apply({ added, changed, removed })
  }
>
  <Paper />
</GraphProvider>
```

## **7. Changing the graph from anywhere with useGraph()**

Before, renaming a node from a toolbar, sidebar, or command palette meant passing `graphRef.current` down through props or building your own context around a `ref`.

‍**Before: manual integration**

```
// DO NOT USE - Old way of integrating JointJS with React

// graphRef is created next to the paper and passed down via every layer in between
function Toolbar({ graphRef, selectedId }: { graphRef: RefObject<dia.Graph | null>; selectedId: dia.Cell.ID }) {
 const rename = (id: dia.Cell.ID, text: string) => {
   graphRef.current?.getCell(id)?.attr('label/text', text);
 };
 return <button onClick={() => rename(selectedId, 'New name')}>Rename</button>;
}
```

**After: JointJS for React**

```
// New native JointJS for React integration

// Any descendant of <GraphProvider>, no graph prop needed
function Toolbar({ selectedId }: { selectedId: string }) {
 const { setCellData } = useGraph();
 return (
   <button onClick={() => setCellData(selectedId, (prev) => ({ ...prev, label: 'New name' }))}>
     Rename
   </button>
 );
}
```

Any descendant of `<GraphProvider>` can reach the graph, with no props threaded through layout components. What you get back is a typed API:

| Method | What it does |
| --- | --- |
| `setCell` / `setCellData` | Add or update a cell, or only its data |
| `removeCell` / `removeCells` | Remove cells by id or reference |
| `resetCells` / `updateCells` | Replace or transform the whole set |
| `exportToJSON` / `importFromJSON` | Serialize and restore the graph |
| `isElement` / `isLink` | Type guards backed by the graph’s type registry |
| `transaction` | Group many edits into one undo entry and one render |
| `graph` | The underlying dia.Graph, when you need it |

## **A simple JointJS for React diagram**

Here’s a small but complete diagram that combines several of these patterns: two nodes, a link, React-rendered nodes, click-to-select, and a button that renames a node from outside the canvas.

```
// New native JointJS for React integration

import { GraphProvider, Paper, HTMLBox, useGraph } from '@joint/react';
import '@joint/react/styles.css';

const initialCells = [
 { id: 'a', type: 'element', position: { x: 40, y: 40 }, data: { label: 'Start' } },
 { id: 'b', type: 'element', position: { x: 280, y: 180 }, data: { label: 'End' } },
 { id: 'ab', type: 'link', source: { id: 'a' }, target: { id: 'b' } },
];

function RenameButton() {
 const { setCellData } = useGraph();
 return (
   <button onClick={() => setCellData('a', (prev) => ({ ...prev, label: 'Renamed' }))}>
     Rename
   </button>
 );
}

export default function Diagram({ onSelect }: { onSelect: (id: string) => void }) {
 return (
   <GraphProvider initialCells={initialCells}>
     <Paper
       style={{ width: '100%', height: '100%' }}
       renderElement={({ label }) => <HTMLBox>{label}</HTMLBox>}
       onElementPointerClick={({ id }) => onSelect(String(id))}
     />
     <RenameButton />
   </GraphProvider>
 );
}
```

There are no refs, effects, teardown calls, or model subclasses. Everything you needed to set up before, from lifecycle and event wiring to measurement and sync, is handled by the graph provider, the paper, and the hooks.

## **Transition to JointJS for React gradually**

You don’t have to rewrite your whole app to try JointJS for React. It’s an integration that uses [@joint/core](https://www.npmjs.com/package/@joint/core) and exposes it, so links, routers, connectors, ports, tools, and the paper transform model all work as before.

To use a pre-existing JointJS graph instance, use the graph prop (`<GraphProvider graph={existingGraph}>`), and you can use `useGraph().graph` to access the underlying `dia.Graph` whenever you need the core API. That way, you can start transitioning your app gradually instead of rewriting everything at once.

## **Conclusion**

Everything outlined in this guide was already possible if you manually wrote it by hand, but with JointJS for React, it’s simpler, much more elegant, and at the end of the day, it’s a lot less code to write and maintain.

To quickly get up to speed with JointJS for React, check one of the following resources:

- [Short guide on the easiest ways to get started with JointJS for React](https://www.jointjs.com/blog/how-to-get-started-with-jointjs-for-react)
- [JointJS for React Quickstart guide in the official docs](https://docs.jointjs.com/react/getting-started/)
- [Start a free trial of JointJS+ for React](https://www.jointjs.com/free-trial)

‍

## **FAQ**

Is core JointJS deprecated now that JointJS for React exists?

What boilerplate does JointJS for React remove?

Do I have to fully rewrite existing diagrams to use JointJS for React?

Can I keep diagram state in Redux, Zustand, or useState?