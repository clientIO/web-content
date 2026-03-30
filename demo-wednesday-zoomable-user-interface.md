---
source: https://www.jointjs.com/blog/demo-wednesday-zoomable-user-interface
generated: 2026-03-30
format: markdown
---

We've published a new demo: [Zoomable User Interface (ZUI)](https://www.jointjs.com/demos/zoomable-user-interface-zui)

There is not just one way to represent hierarchical diagrams. You can represent a hierarchy in a single diagram and nest each level of the hierarchy deeper into their parents, or you can isolate each level using UI widgets such as windows or tabs, and then allow the user to switch between them. While the use of tabs allows users to focus on each level without too many distractions, it makes it difficult to see the overall picture of the hierarchy. It’s also a relatively simple option to implement, as shown by one of our previous examples - tabs.

On the other hand, displaying a hierarchy in a single diagram can be cluttered with too much information.Techniques such as node collapsing/uncollapsing can be adopted to hide unnecessary details. The difficult part of this approach could be the automatic rearrangement of nodes when they are expanded/collapsed and thus resized.

An alternative approach to collapsible containers is a zoomable user interface (ZUI) that first provides an overview and then on demand gives details via zooming. The ZUI is the subject of today’s demonstration.

In this approach, nodes are progressively smaller with increasing depth. Each deeper level must be rendered at a smaller scale (this includes not only shapes, fonts, outlines, but also element tools and links). We didn’t feel like going this path, so we decided to experiment a bit. We define each level as a separate diagram (i.e. in the same way as with tabs) and when the user zooms in on the container, we dynamically replace the contents of the diagram with a child diagram. Conversely, when the user zooms out of the container, we replace the current diagram with the parent diagram and only display images of the child diagrams inside the zoomable elements.

‍

**Interested in enhancing your application with interactive diagrams?** [Start a free JointJS+ trial](/free-trial) and build visual and No-Code/Low-Code applications with easy and confidence.

Every Wednesday we share diagramming tips, interesting features and news in JointJS. Learn with us, get content delivered straight to your inbox and become a real diagramming pro: