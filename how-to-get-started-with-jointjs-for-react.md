---
source: https://www.jointjs.com/blog/how-to-get-started-with-jointjs-for-react
generated: 2026-08-18
format: markdown
---

Whether you’re experimenting, building a proof of concept, or ready for a production-grade app, this roadmap will help you find the right starting point.

We just released [JointJS for React](https://docs.jointjs.com/react) and [shared a bit about who it is for, why it matters, and why you should start using it](https://www.jointjs.com/blog/introducing-jointjs-for-react).

In this article, you’ll get a practical, hands-on guide on getting started with JointJS for React. We won’t go into nitty-gritty details here, but instead we’ll give you a clear outline of the best ways you can jump into it without much effort.

We’ll briefly cover:

- How to start from a ready-made demo ([AI Workflow Builder](https://www.jointjs.com/demos/ai-workflow-builder)) and customize it for your project
- Guidance on building your first app step-by-step using the documentation and quickstart guide
- How to use AI Coding Agents to accelerate development, along with quick installation instructions to get you up and running
- A conclusion with tips, next steps, and further resources

## **Start with the AI Workflow Builder demo**

Instead of building your app from scratch, the best way to start is to use one of the existing JointJS for React demos that’s close to your actual needs, such as AI Workflow Builder, to build your own proof of concept JointJS for React app.

‍

First, we’ll set up an AI Workflow Builder demo project in a new folder. You can download it using the JointJS CLI tool:

```
npx @joint/cli download ai-workflow-editor/react
```

‍

Alternatively, you can simply clone the [AI Workflow Builder demo GitHub repository](https://github.com/clientIO/joint-demos/archive/refs/heads/main.zip).

Once the demo is downloaded, run npm install to set up all project dependencies. Note that this demo is built in JointJS+ for React, the commercial extension of the open-source, community-driven library, which installs from the private JointJS npm registry, so you’ll need an access token in the `.npmrc` file to install it.

You can get the access token in our [customer portal](https://my.jointjs.com/login) or by starting your [free trial of JointJS+](https://www.jointjs.com/free-trial). You can find [more info on setting up the access token in the docs](https://docs.jointjs.com/learn/help-center/npm-registry/).

Once you’ve successfully installed the dependencies, run the npm run start command to start the development server. By default, it will start on localhost, port 5173 (http://localhost:5173/).

Once you have the demo set up, you can either explore the codebase yourself or ask your AI Coding Agent to give you a detailed overview of the project:

```
Give me an overview of this JointJS+ for React codebase, focusing on JointJS and the key things I need to know about the app.
```

‍

As expected, Claude Code, the AI Agent I’m using for this demo, examined the codebase in detail and provided a clear overview of key concepts and everything you need to dig into it yourself.

An example output of a prompt requesting an overview of JointJS for React codebase.

‍

You can now start tweaking the demo yourself, or better yet, follow up with your AI Coding agent to precisely tweak it to suit your needs.

I recommend you use the [JointJS MCP Server](https://docs.jointjs.com/learn/help-center/mcp-server/) to get direct access to the latest, up-to-date JointJS docs. Even without the MCP server, your AI coding agent will be able to figure out precisely what it needs to do by analyzing JointJS code, but using the MCP server is more efficient and will get you better results in the end.

Also, if you’re using JointJS MCP Server, you don’t have to manually clone the demo; you can just ask AI to tweak the JointJS for React AI Workflow Builder demo, and AI will set up everything for you.

## **Build your first app step by step by following our quickstart guide**

Using AI Coding agents to tweak one of our prebuilt demos is the simplest and most efficient way of starting if you’re building a proof of concept and plan to build a serious, production-grade app.

But if you want to learn more about JointJS for React, if you want to understand key concepts to be able to review AI agent’s changes and to be able to direct your AI coding agent better, it’s best to get your hands dirty by following our [JointJS for React Quickstart Guide](https://docs.jointjs.com/react/getting-started/) in the docs.

The guide is structured into multiple chapters, and each chapter focuses on one key concept, so it’s easy and straightforward to follow:

1. Install @joint/react: add the package, import the styles, and size the canvas.
2. Build your first diagram: render elements from plain data.
3. Add and update elements: read the graph and change it while the app runs.
4. Create custom elements: rich, data-driven nodes with ports, styled your way.
5. Connect elements with links: arrowheads, labels, and routing.
6. Make the canvas interactive: dragging, clicks, and selection.
7. Zoom and pan the canvas: an infinite, scrollable, zoomable viewport with JointJS+.
8. Add an element palette: drag from a palette onto the canvas.
9. Add a property editor: edit the selected node from a live inspector.
10. Add an element overlay: React UI anchored to an element, such as a badge, toolbar, or popover.
11. Add a minimap: a bird’s-eye view that tracks the canvas.

The quickstart guide is designed to be straightforward and approachable for everyone, clearly outlining all key concepts of the library as you encounter them.

By the end of the guide, you’ll build a complete workflow editor that includes all the key features you’ll find in flowcharts and diagrams, from palette, canvas, minimap, to a live properties panel, giving you insight into JointJS open-source and JointJS+ commercial features.

A final state of a diagramming app built by following JointJS for React quickstart guide.

## **Use AI Coding agents to set up your JointJS for React project from scratch**

If you want to start completely from scratch, or add JointJS for React to your existing project, install the library directly from NPM. The open-source version of the library is available at @joint/react, and the commercial extension, JointJS+ for React, is available on NPM at `@joint/react-plus`.

### **Install JointJS for React through NPM**

For this demo, we’ll start from scratch and use the Vite build tool to set up a simple React project:

```
npm create vite@latest jointjs-for-react-demo -- --template react-ts
```

‍

Next, we need to install JointJS for React, the open-source version of the library. The package is available at [@joint/react](https://www.npmjs.com/package/@joint/react?activeTab=readme):

```
npm install @joint/react
```

‍

This will work with any modern React setup, so you can easily drop it into Vite, Next.js, Remix, and so on. Just as well, you can use JointJS+ for React instead of the open-source version.

```
npm install @joint/react-plus
```

‍

For this guide, we’ll use the open-source version of the library, but JointJS+ for React includes everything from JointJS for React and works exactly the same (the only difference being that `<GraphProvider />` in  JointJS+ becomes `<Diagram />`. And of course, it also gives you access to selection, history, clipboard, spatial index, and more.), just with an expanded set of features.

Once our React project is up and running and the JointJS for React package is installed, we'll set up a simple JointJS canvas. The easiest way to start is to use an AI Coding agent to set up the boilerplate project.

### **Set up a basic JointJS canvas with your AI Coding agent**

Most developers these days use AI Coding Agents extensively in development, just as they should. And this is precisely where JointJS for React shines. JointJS for React is strongly typed, so your AI Coding agents can easily parse the library and understand exactly how it works and how it can give you the result you want.

You can feel confident using JointJS for React even if you don’t want to wait for the AI training sets to update and kick in with new [JointJS for React docs](https://docs.jointjs.com/react/). Better yet, you can install [JointJS MCP Server](https://docs.jointjs.com/learn/help-center/mcp-server/), which provides direct access to up-to-date JointJS docs, including React, to achieve higher-quality code overall.

```
Replace the React demo and build a @joint/react app with a canvas graph, paper, and two rectangles I can drag. Add one input port on the left and one output port on the right to the rectangles, and draw a link from the output port of the first rectangle to the input port of the second rectangle.

Make the styling slick, modern, and clean with plenty of padding.
```

Note that I’m explicitly mentioning the *@joint/react* package so the AI Coding Agent knows exactly what to use. I’m using Claude Code in this article, but this will work with any other setup as well.

An example of a JointJS for React app built with an AI Coding Agent through a single prompt.

​

AI Agent set up a simple JointJS for React canvas and configured the app precisely as it needs to:

```
import { GraphProvider, Paper, HTMLHost, linkRoutingSmooth, type ElementPort, type CellRecord } from '@joint/react';
import '@joint/react/styles.css';
import './App.css';

function App() {
  return (
    <div className="canvas-page">
      <header className="canvas-header">
        <h1>JointJS + React</h1>
        <p>Drag the rectangles around the canvas</p>
      </header>
      <div className="canvas-frame">
        <GraphProvider initialCells={initialCells}>
          <Paper
            renderElement={RectangleNode}
            linkRouting={linkRoutingSmooth()}
            defaultLink={{ style: { color: '#7c3aed', width: 2.5, targetMarker: 'arrow' } }}
            gridSize={20}
            drawGrid={{ name: 'dot', args: { color: '#d8d3e6', thickness: 1.5 } }}
            background={{ color: '#faf9fc' }}
            className="canvas"
          />
        </GraphProvider>
      </div>
    </div>
  );
}

export default App;
```

‍

The `RectangleNode` function is responsible for turning the element’s data into React UI. It uses `HTMLHost` so the element can be plain HTML:

```
function RectangleNode({ label, hint }: NodeData) {
  return (
    <HTMLHost useModelGeometry className="node">
      <span className="node__hint">{hint}</span>
      <span className="node__label">{label}</span>
    </HTMLHost>
  )
}
```

‍

And the initial elements, ports, and links are configured in their own constants:

```
type NodeData = {
  label: string
  hint: string
}

const ports: Record<string, ElementPort> = {
  in: {
    cx: 0,
    cy: '50%',
    width: 16,
    height: 16,
    color: '#ffffff',
    outline: '#c4b5fd',
    outlineWidth: 2,
    passive: true,
},
  out: {
    cx: '100%',
    cy: '50%',
    width: 16,
    height: 16,
    color: '#7c3aed',
    outline: '#ffffff',
    outlineWidth: 2,
  },
}

const initialCells: CellRecord<NodeData>[] = [
  {
    id: 'rect-a',
    type: 'element',
    position: { x: 120, y: 160 },
    size: { width: 220, height: 120 },
    portMap: ports,
    data: { label: 'Rectangle A', hint: 'Output' },
  },
  {
    id: 'rect-b',
    type: 'element',
    position: { x: 560, y: 160 },
    size: { width: 220, height: 120 },
    portMap: ports,
    data: { label: 'Rectangle B', hint: 'Input' },
  },
  {
    id: 'rect-a-rect-b',
    type: 'link',
    source: { id: 'rect-a', port: 'out' },
    target: { id: 'rect-b', port: 'in' },
    style: {
      color: '#7c3aed',
      width: 2.5,
      targetMarker: 'arrow',
    },
  },
]
```

‍

From here, you can use your AI Coding Agent to tweak and extend it according to your precise project needs. Follow up in your initial prompt to get the result you’re looking for.

# **Conclusion**

If you want to quickly build a proof of concept for your own use case with JointJS for React, start with the AI Workflow Builder demo and use AI coding agents to tweak it to suit your needs.

If you want to understand a bit more about how JointJS for React works, follow our [Getting Started Guide](https://docs.jointjs.com/react/getting-started/) in the docs, and in the few short lessons, you’ll learn everything you need to get confident in building production-grade diagramming and flowchart apps.

## **Ready to get started?**

- [Explore the official JointJS for React documentation for detailed guides and API references](https://docs.jointjs.com/react)
- [Try the AI Workflow Builder demo](https://www.jointjs.com/demos/ai-workflow-builder)
- [Learn more about JointJS+ and start a free trial](https://www.jointjs.com/free-trial)

These resources will help you take your next steps and get the most out of JointJS for React and JointJS+ for React.

Happy diagramming!

‍

## FAQ

What is the recommended way to start building with JointJS for React?

How do I install JointJS for React in a new or existing project?

What’s the difference between JointJS for React and JointJS+ for React?

Can I use AI Coding Agents with JointJS for React?

How can I learn the basics and key concepts of JointJS for React?

Do I need a commercial license to try JointJS for React?

Where can I find more resources?