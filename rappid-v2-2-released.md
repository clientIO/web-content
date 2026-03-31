---
source: https://www.jointjs.com/blog/rappid-v2-2-released
generated: 2026-03-31
format: markdown
---

We're pleased to announce a new update to the JointJS+ library, version 2.2, full of updates, fixes, and some great new features.

In particular, JointJS+ v2.2 adds two new plugins for editing and drawing lines and curves. This opens up all sorts of new possibilities for building apps with vector editing capabilities similar to what you can find in programs like Adobe Illustrator, Sketch, Inkscape and others.

Combining these new capabilities with the additional features of JointJS+, one can build full-fledged vector graphics editors and diagram builders where users can draw engineering parts, or simply add freehand sketching capabilities to flowcharting, workflows and other diagramming apps built with JointJS+.

## JointJS+ 2.2 Highlights:

‍

### New ui.PathEditor plugin for editing vector SVG paths.

‍

‍

‍

### New i.PathDrawer plugin for drawing SVG paths.

‍

‍

‍

### New [Vector Editor demo app](https://www.jointjs.com/demos/vector-editor) for PathEditor and PathDrawer, effectively implements a simple vector graphics editor.

‍

‍

### JointJS+ v2.2 is compatible with both Lodash v3 and v4.

‍

‍

‍

‍

‍

### Download JointJS+ v2.2 and start editing vectors with ease, thanks to our new [Vector Editor demo app](https://www.jointjs.com/demos/vector-editor).

‍

‍

‍

‍

‍

‍

## Complete JointJS+ v2.2 Changelog

- [new VectorEditor demo app demonstrating PathEditor and PathDrawer](https://www.jointjs.com/demos/vector-editor) - LIVE DEMO!
- [automatic directed graph layout adds support for link labels](https://www.jointjs.com/demos/directed-graph-layout) - LIVE DEMO!
- ui.PathEditor - new plugin for editing SVG paths
- ui.PathDrawer - new plugin for drawing SVG paths
- JointJS+ compatible with Lodash v3 and v4
- add TypeScript definitions
- KitchenSink demo app - fix Safari link connection points bug
- fix svg/png export performance
- OrgChart - improve demo with new `event` attribute
- ui.Halo - prevent errors when halo removed while dragging
- ui.Halo - add `magnet` option for specifying link source/target magnet
- ui.Inspector - fix content-editable focus in Firefox
- ui.Inspector - allow `type` property to be edited
- ui.Inspector - select-box, color-palette and select-button-group options can be defined as path
- ui.Inspector - enable `when` expressions for groups
- ui.Inspector - fix "ui.Inspector: can not read value of removed select-box" error
- ui.Selection - `selection-box` event handlers called with `x` and `y` coordinates
- ui.Stencil - fix clone position while dragging
- ui.Stencil - add `paperOptions` option to modify stencil papers
- ui.Stencil - fix scrolling on touch devices
- ui.PaperScroller - improve transitions in IE
- ui.Keyboard - support for function keys
- format.Raster - fix for `image` tags without href attr
- format.Raster - add check for size limit of canvas
- format.SVG - add `area`, `useComputedStyles` and `stylesheet` options
- format.SVG - honors the current prefix for the viewport selector
- layout.GridLayout: add `deep`, `parentRelative` options
- layout.GridLayout: add `compact` type for `columnWidth` and `rowHeight`
- layout.TreeLayout: add `firstChildGap` element attribute
- shapes.BPMN - add `ratio` option for Pool lanes
- shapes.BPMN - fix Choreography rendering issues and links in Firefox

We hope you you'll get the most from these new features, fixes and updates. Please don't hesitate to [get in touch](/cdn-cgi/l/email-protection#402f322700232c29252e346e292f7f3335222a2523347d122130302924657270726e716e706572703135253334292f2e) with questions or comments.

‍

Happy diagramming!

*- The JointJS Team*