---
source: https://www.jointjs.com/blog/releasing-4-2
generated: 2026-03-22
format: markdown
---

**This release focuses on guided, layout-driven diagram editing — where elements are positioned automatically rather than through free drag-and-drop. It also introduces a new Layers API for structured, multi-level diagrams, major performance improvements for large graphs, and seven new boilerplate apps to help you build faster.**

👉 Version 4.2 includes many updates, which we’ll cover briefly in this post. For a deep dive into all the technical details, [check out the full changelog](https://docs.jointjs.com/learn/release-notes/4.2.0).

*"Until now, JointJS has focused primarily on free-style drag-and-drop interactions, giving users maximum flexibility when creating diagrams. While that freedom is valuable, it can also add complexity. Layout-driven diagramming, on the other hand, helps users focus on what’s most important — the workflow logic — and makes diagrams more accessible to less technical users. This release makes it easier to build these guided diagrams with less boilerplate, and ships with example applications emphasizing user experience. Thanks to the latest performance improvements, you can now render tens of thousands of elements instantly, with the library managing resources efficiently under the hood. But what excites me most about this release is the new Layers API, which unlocks fresh possibilities within our library." says Roman Brückner, the company’s CTO.*

### ⭐ New demo applications

**We’ve added seven advanced applications ready to use in your project!** Existing customers with active update subscriptions can find their source code in the latest package, and anyone else eager to explore the newest features can [start a free 30-day trial](/free-trial) for full access to the latest version.

#### AI Agent builder

**Empower users to design AI Agents through a simple-to-use interface** embedded in your web app. The new AI Agent builder boilerplate uses layout-driven diagram editing to automatically arrange elements, keeping workflows clear and intuitive while allowing users to integrate apps, add logic, and define behaviors effortlessly.

👉 [Play with the demo app](https://www.jointjs.com/demos/ai-agent-builder)

#### BPMN Editor

Modeling business processes has become even easier with the new JointJS-powered BPMN Editor. The latest release introduces a **major redesign along with new features**, including a minimalist element palette, new shapes, a dynamic minimap, and a tabbed property editor and viewer.

👉 [Play with the demo app](https://www.jointjs.com/demos/bpmn)

#### Fishbone

The next app showcases a Fishbone (Ishikawa) diagram — a visual tool for **identifying and organizing potential root causes of a problem**. It helps teams break down issues into clear categories — such as Material, Machine, Management, or Environment — making it ideal for root cause analysis and collaborative problem-solving.

👉 [Play with the demo app](https://www.jointjs.com/demos/fishbone)

#### PERT chart

Effective project management depends on clear visualization. The new PERT chart demonstrates key JointJS+ features such as zoom and pan, automatic layout, events, and custom shapes.

👉 [Play with the demo app](https://www.jointjs.com/demos/pert-chart)

*⭐ We’ve taken it a step further by introducing a PERT chart integrated with* [*Bryntum’s Gantt chart*](https://bryntum.com/products/gantt)*. Explore their synergy in* [*our demo app*](https://www.jointjs.com/demos/bryntum-integration)*.*

#### Timeline

This timeline demo takes you through key milestones of OpenAI and Anthropic while showcasing **advanced diagramming features** in JointJS+. Delete events, or add new ones to reshape the history of leading AI companies.

👉 [Play with the demo app](https://www.jointjs.com/demos/timeline)

#### Cables

**Need to create interactive wiring diagrams?** Check out our Cables demo, built with JointJS+ and TypeScript. It starts with a simple example — a cable connected to a terminal block — showcasing the core capabilities of the library.

👉 [Play with the demo app](https://www.jointjs.com/demos/cables)

### ELK Layout

The new ELK Layout demo, written in TypeScript, shows how to use the [elkjs](https://github.com/kieler/elkjs) library with JointJS to generate automatic diagram layouts powered by the **Eclipse Layout Kernel (ELK)**.

👉 [Play with the demo app](https://www.jointjs.com/demos/elk-automatic-layout)

‍

### 🟦 Layers API

In 4.2, we introduced a new Layers API, which required a substantial internal refactor of the Graph.

The Graph now consists of multiple layers, where each layer is its own model with independent attributes and its own cell collection. Every layer maintains its own stacking context for z-index ordering. Layer configurations are serializable, so any changes can be exported and loaded back.

**Applications can now leverage layer support to modify layers, control visibility, and handle interactivity**, as shown in the example.

👉 [Read more in our changelog](https://docs.jointjs.com/learn/release-notes/4.2.0/#layers-api)

‍

### 🚀 Optimized rendering and memory management for large diagrams

Previously, views were created as soon as their models were added to the graph, consuming memory even if those views were never shown. In this release, **view instantiation is deferred until the moment the view is actually needed** — for example, when it becomes visible on the screen or when a collapsed branch is expanded. Views that are no longer needed can also be disposed, freeing resources and allowing the garbage collector to reclaim memory.

We've also introduced **built-in virtual rendering support**, enabled with a single boolean. It leverages SearchGraph to quickly determine which views should be visible at any given moment. When loading a large diagram where only a subset is exposed, the system can now efficiently locate, create, and render only the views currently relevant.

In the example below, **rendering 19,999 elements takes just 0.24 seconds**, delivering a smooth and responsive experience.

Rendering diagrams outside the DOM is now available and the asynchronous rendering should now always be used together with the revamped autoFreeze option, which automatically puts the system to sleep when no work remains — reducing battery usage and allowing garbage collection to occur sooner.

👉 [Read more in our changelog](https://docs.jointjs.com/learn/release-notes/4.2.0/#optimized-rendering-and-memory-management)

‍

### ⚙️ Other updates

#### **Microsoft Automatic Graph Layout (MSAGL)**

We’ve introduced a new layout package based on **Microsoft Automatic Graph Layout** to automatically organize complex diagrams for improved clarity and efficiency.

👉 [Read more in our changelog](https://docs.jointjs.com/learn/release-notes/4.2.0/#msagl)

#### Inspector & CommandManager support for any model

Previously, the graph was the sole source of truth for editing operations. In this release, **any model can now act as the primary editable source**. This means it can be inspected, modified through the Inspector, and its changes can be tracked and reverted using the CommandManager, just like graph-level edits.

👉 [View a diagram illustrating this concept in our changelog](https://docs.jointjs.com/learn/release-notes/4.2.0#guided-layout-driven-diagram-editing)

‍

### 💪 As always, there is more...

We’ve highlighted some of the key updates in version 4.2, but there’s plenty more to discover. Dive into the full release and start building powerful visual applications effortlessly.

[Read full changelog](https://docs.jointjs.com/learn/release-notes/4.2.0)

‍

### 🔵 JointJS for React as our next milestone

As you may have noticed, we’ve already released the [Alpha version of JointJS for React](https://github.com/clientIO/joint/discussions/3010), making a significant step towards React enthusiasts who weren't satisfied with our wrapper. After the 4.2 release, we've taken a quick break for a good coffee, and are back with full power to deliver production-ready React version of JointJS in the upcoming weeks — stay tuned!

And if you're ready to build with the latest version of our library, take one of these routes to get started:

- JointJS+ customers can download the latest package in [our customer portal.](https://my.jointjs.com/)
- Non-customers can [start a free 30-day trial](/free-trial) to access the latest features and improvements and evaluate JointJS+ for their project.

**Excited to shape the future of diagramming with us?** [Share your ideas for new features and improvements on our GitHub](https://github.com/clientIO/joint/discussions/categories/ideas) and influence what the next JointJS and JointJS+ versions will look like.

Happy diagramming! 🙌