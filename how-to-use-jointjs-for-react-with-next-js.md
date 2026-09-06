---
source: https://www.jointjs.com/blog/how-to-use-jointjs-for-react-with-next-js
generated: 2026-09-06
format: markdown
---

If you’re wondering if you can use the JointJS for React library with the Next.js framework, the answer is a clear and resounding yes. In this post, you’ll learn everything you need to start using JointJS for React with Next.js, along with a crucial setup detail, and along the way you’ll pick up some tips for building your own production-grade diagramming applications.

## Demo setup (a simple Next.js app)

First, we’ll set up a simple Next.js application. If you haven’t already, create a new Next.js project through your terminal:

```
npx create-next-app@latest jointjs-next-demo
cd jointjs-next-demo
```

JointJS for React is available on NPM, so you can easily add it to your project:

```
npm install @joint/react
```

After installation, you’ll see `@joint/react` listed as a dependency in your package.json. At the time of writing, the latest version is 4.3.5.

Note that JointJS+ for React is available in a private NPM registry, so you’ll need an access token to use it:

```
npm install @joint/react-plus
```

You can find the guide on using the JointJS private NPM repository and setting up your access token in the docs: [Using JointJS NPM Repository](https://docs.jointjs.com/learn/help-center/npm-registry)

**Already a JointJS+ customer?**

Download the latest package, including JointJS+ for React, [using npm](https://docs.jointjs.com/learn/help-center/npm-registry) or from our [customer portal](https://my.jointjs.com/). If your update subscription expired, [reach out to us](https://www.jointjs.com/contact-us) for re-activation.

**New to JointJS+?** Start a [30-day no-commitment trial](https://www.jointjs.com/free-trial), which now includes JointJS+ for React.

## Integrating JointJS for React in your Next.js project

Once you install JointJS for React, you’ll need to import the necessary components from the library along with the stylesheet into your application.

For this article, we’ll use the code from the [JointJS for React Quickstart guide](https://docs.jointjs.com/react/getting-started/). We’ll go step by step, so first, we’ll import everything we need for this demo. Open your main app file, typically `app/page.tsx`, and replace the default import (`import Image from "next/image";`) with the following:

```
import { GraphProvider, Paper, HTMLBox } from '@joint/react';
import '@joint/react/styles.css';
```

We’ll use `GraphProvider`, `Paper`, and `HTMLBox` components to render the JointJS diagram, and style.css for default styling.

## Setting up your first JointJS diagram in a Next.js app

Next, remove all default content from the `return` statement and add code from the quickstart guide:

```
export default function Home() {
  
  // Cells used to create the initial graph at mount
  const initialCells = [
    { id: '1', type: 'element', position: { x: 300, y: 140 }, data: { label: 'Hello' } },
    { id: '2', type: 'element', position: { x: 500, y: 200 }, data: { label: 'Next.js' } },
    {
      id: '1→2',
      type: 'link',
      source: { id: '1' },
      target: { id: '2' },
      style: { targetMarker: 'arrow' },
    },
  ];

  return (
      <main>
         <GraphProvider initialCells={initialCells}>
          <Paper
            renderElement={({ label }) => <HTMLBox>{label}</HTMLBox>}
            style={{ height: 400 }}
          />
        </GraphProvider>
      </main>
  );
}
```

As we want the entire app to be a diagram, we’ll additionally tweak the style of the `<Paper />` component: `style={{ height: '100vh', width: '100%' }}`. We’ll use Viewport Height units to ensure the diagram takes up 100% of the browser window's height. Note that `height: 100%;` will not work, as it requires a concrete height set on the parent element.

## The most important setup detail to use JointJS for React in Next.js projects

This is all you need for a simple JointJS for React app. But if you try to run it in the browser, you’ll get an error:

*An example of a Runtime TypeError caused by JointJS for React if you don't include the 'use client' directive in your Next.js component.*

As it’s clearly outlined in the error message, JointJS for React is a client-side library, so you’ll need to add the `'use client';` directive to the top of the file because Next.js, by default, renders components on the server. The directive tells Next.js to render the component on the client side

When we add the `'use client';` directive, the full demo code will look like this:

```
'use client';

import { GraphProvider, Paper, HTMLBox } from '@joint/react';
import '@joint/react/styles.css';

export default function Home() {
  const initialCells = [
    { id: '1', type: 'element', position: { x: 300, y: 140 }, data: { label: 'Hello' } },
    { id: '2', type: 'element', position: { x: 500, y: 200 }, data: { label: 'Next.js' } },
    {
      id: '1→2',
      type: 'link',
      source: { id: '1' },
      target: { id: '2' },
      style: { targetMarker: 'arrow' },
    },
  ];

  return (
      <main>
         <GraphProvider initialCells={initialCells}>
          <Paper
            renderElement={({ label }) => <HTMLBox>{label}</HTMLBox>}
            style={{ height: '100vh', width: '100%' }}
          />
        </GraphProvider>
      </main>
  );
}
```

‍

And this is what our interactive diagramming demo app will look like:

A screenshot of a simple JointJS for React diagram using in Next.js app.

## Your next steps with JointJS for React

Now that you know how to make JointJS for React work with Next.js, you can continue following our [Quickstart Guide](https://docs.jointjs.com/react/getting-started/) to become familiar with all the key concepts, or try one of the following:

- **AI Coding Agents:** JointJS works seamlessly with AI coding agents like Claude Code. You can prompt these tools to help you build complex diagrams with JointJS for React effortlessly.
- **JointJS MCP Server:** If you want to get the most out of your coding agents, set up the JointJS MCP Server. You’ll find links to all documentation and resources in our [Introduction to JointJS MCP Server guide](https://www.jointjs.com/blog/introducing-jointjs-mcp-server).
- **Other React Frameworks:** If you’re using another React-based framework, the key takeaway is that JointJS is a client-side library. Set up client-side rendering in your framework, just as you did here with Next.js, and you’ll be ready to create production-grade diagrams using JointJS for React.
- [**Start your JointJS+ Free Trial**](https://www.jointjs.com/free-trial)**:** If you’re building serious, production-grade diagramming applications, check out JointJS+ for React, a commercial extension of JointJS for React, which will drastically speed up your development and give you premium components you can easily use in your applications.

## Conclusion

Getting JointJS for React running in your Next.js application is straightforward. The only thing you really need is the use client directive at the top of components where you set up your diagrams. For more details and advanced topics, check out our JointJS for React [Quickstart guide](https://docs.jointjs.com/react/getting-started/) and [documentation](https://docs.jointjs.com/react/).

Happy diagramming!