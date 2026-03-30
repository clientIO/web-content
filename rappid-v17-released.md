---
source: https://www.jointjs.com/blog/rappid-v17-released
generated: 2026-03-30
format: markdown
---

### The highlight of **JointJS+ 1.7** release is the following three features:

- ‍**a powerful and efficient graph data model with traversing algorithms**,**‍**
- **a flexible tree layout engine** and**‍**
- **improved inline text editing**.

Read further to find out what else has been added in the new version of JointJS+ HTML 5 diagramming toolkit. JointJS+ gives you all the tools you need to build state-of-the-art products integrating visual interfaces for editing workflow, BPMN and flowchart diagrams, among others.

## New features

### A Powerful Graph Data Model

The JointJS+ core graph data model has been extended with many functions dealing with traversing directed graphs and accessing structural information. For this, we have implemented an efficient representation of the graph allowing us to make fast lookups. The following is a list of some of the new functions available on the graph object:

- dfs() (Depth-first search algorithm)

- bfs() (Breadth-first search algorithm)

- isSuccessor(), isPredecessor(), isNeighbor(), getPredecessors(), getSuccessors(), getSubgraph()
- isSource(), isSink(), getSources(), getSinks()
- cloneCells(), cloneSubgraph()

All these functions not only work on flat graphs but also hierarchical ones.

### Flexible Tree Layout Engine

[TreeLayout](https://resources.jointjs.com/docs/rappid/v3.3/layout.html#layout.TreeLayout) and its accompanying [TreeLayoutView](https://resources.jointjs.com/docs/rappid/v3.3/layout.html#layout.TreeLayout) now support not only left-to-right, right-to-left but also top-to-bottom and bottom-to-top layout types.

It is even possible to have different intermixed layout types on a per-node basis!

### Improved Inline Text Editing

The [TextEditor](https://resources.jointjs.com/docs/rappid/v3.5/ui.TextEditor.html) component, which implements powerful SVG inline text editing of any text in any diagram object, now uses native browser selections and supports editing of link labels (rich-text and rotated text too!). The native browser selection has made selecting large amounts of text much more efficient with smoother, more-comfortable user interaction.

Improved inline editing of link labels is another great addition and can be enabled literally in four lines of code.

## ... and much more!

- [Inspector](https://resources.jointjs.com/docs/rappid/v3.5/ui.Inspector.html) widget now provides an easy way to add custom field types.
- [PaperScroller](https://resources.jointjs.com/docs/rappid/v3.5/ui.PaperScroller.html) introduces new methods scroll(), scrollToElement() andcenterElement() for programmatic scrolling (even animated)
- [Halo](https://resources.jointjs.com/docs/rappid/v3.5/ui.Halo.html) control panel has been improved and extended with a way to display more than one pie menu toggle at the same time
- [dia.Paper](https://resources.jointjs.com/docs/jointjs/v3.6/joint.html#joint.dia.Paper:options.multiLinks) adds a new option multiLinks as a quick way to switch off the possibility to create two links connecting the same elements
- [A critical bug](https://www.jointjs.com/blog/announcement-gettransformtoelement-polyfill) fix for an upcoming version of Google Chrome which removed the native getTransformToElement() method on SVG elements
- ... and there's more!

See the JointJS+ 1.7 CHANGELOG page for full details.

##### [BUY JOINTJS+ AND BUILD GREAT APPS NOW!](https://www.jointjs.com/jointjs-plus)

If you missed our previous release, visit our blog post to see what components were added and which ones were improved in [JointJS+ 1.6](https://www.jointjs.com/blog/rappid-v16-prague-released) version.