---
source: https://www.jointjs.com/blog/rappid-3-0-is-here
generated: 2026-03-26
format: markdown
---

JointJS+ 3.0 is released and comes with updates, fixes, and great performance improvements.

> *"Our users requested support for ES6 modules and here we have it. We're excited our users can now use JointJS+ in modern build pipelines." says Roman Bruckner, CTO of client IO. "And that's not all! Huge performance gains with smart viewport matching and link-to-link connections make JointJS+ a truly powerful tool."*

You can download the update package from your [Account portal](https://my.client.io). If you're not eligible for a free update you can purchase it through our [online store](https://www.jointjs.com/pricing) or request a free [30 day trial](https://www.jointjs.com/free-trial) to try it out.

Take a look at the main highlights here and the full changelog below.

## JointJS+ 3.0 Highlights:

### Support for ES6 Modules

- Import JointJS+ using ES6 modules syntax.
- Use JointJS+ in modern build pipelines.
- Import only modules/plugins that you need.

‍

‍

‍

‍

‍

‍

‍

‍

‍

‍

### Performance Improvements

- Smart viewport matching algorithm that renders only those shapes visible in the viewport.
- Shapes outside the viewport are not rendered saving a huge amount of render time with large diagrams.
- Viewport re-renders automatically when zooming and panning without the user noticing. See the Collapse/Expand demo: <https://www.jointjs.com/demos/collapse-expand>
- Paper freeze/unfreeze allowing you to control when the paper should re-render.

‍

‍

‍

‍

‍

‍

‍

### Link-to-link Connections

- Links can now be connected to other links.
- Graph algorithms introduce new options to walk through the graph structure with link-to-link connections.
- Check out our new demo on link-to-link connections at <https://www.jointjs.com/demos/mix-bus>

‍

‍

‍

‍

‍

‍

## Complete JointJS+ v3.0 Changelog:

- add Collapsible application
- upgrade dependencies (Backbone v1.4.0, Dagre v0.8.4, Graphlib v2.1.6, jQuery v3.4.1)
- compatibility warnings (https://github.com/clientIO/joint/releases/tag/v3.0.0)
- full support for ES Modules
- support for Link to Link connections
- ui.TreeLayoutView - add `validateConnection`, `reconnectElements`, `translateElements`, `paperConstructor` and `paperOptions` options
- ui.PaperScroller - define `contentOptions` as a function
- ui.PaperScroller - fix unnecessary scrollbars
- ui.Stencil - define `search' option as a function
- ui.Stencil - trigger `group:open` and `group:close` events
- ui.SelectButtonGroup - add `singleDeselect` and `noSelectionValue` option
- ui.Clipboard: fix copy&paste with localStorage
- ui.Halo - support for connectionStrategy
- ui.Halo - add `rotateEmbeds` options
- ui.Inspector - fix content-editable sanitizing
- format.Print - prevent other plugins from being printed
- layout.ForceDirected - add `x`, `y` options, `graph` accepts an array of cells
- layout.TreeLayout - add `getLayoutBBox()`
- layout.TreeLayout - fix `BL`, `TL`, `BR`, `TR` layout link routes not taking element `margin` into account
- dia.CommandManager - fix batch commands sorting
- dia.Paper - async mode revamped (viewport matching, rendering progress) [breaking change]
- dia.Paper - cells are rendered into the `paper.cells` (previously called `paper.viewport`), transformations are applied to `paper.layers` (parent of `paper.cells`) [breaking change]
- dia.Paper - implement viewport matching (remove views from the DOM when not in the viewport) via `viewport` option and checkViewport()
- dia.Paper - add freeze(), unfreeze(), isFrozen() and option `frozen` to stop/start views updates
- dia.Paper - add requireView(), dumpViews(), updateViews() to force views to update
- dia.Paper - add sorting options (none, approximate, exact)
- dia.Paper - add `anchorNamespace`, `linkAnchorNamespace`, `connectionPointNamespace`, `defaultLinkAnchor` options
- dia.Paper - add `useModelGeometry` for scaleContentToFit(), fitToContent(), getContentBBox(), getContentArea()
- dia.Paper - add `contentArea` for scaleContentToFit(), fitToContent()
- dia.Paper - fitToContent() returns area (g.Rect) of the content
- dia.Graph - add `indirect` option for getNeighbors(), getConnectedLinks(), isNeighbor() for link-link connections
- dia.Graph - getBBox() accepts no parameters and returns the bounding box of the entire graph [breaking change]
- dia.Graph - getCellsBBox(cells) does not ignore links passed via `cells` parameter [breaking change]
- dia.Link - add `priority` attribute for anchors
- dia.Link - add getSourceCell(), getTargetCell(), getPolyline(), getSourcePoint(), getTargetPoint(), getBBox()
- dia.Link - getSourceElement() and getTargetElement() finds also indirect elements
- dia.Link - add angle, keepGradient and ensureLegibility options for labels
- dia.ElementView - add findPortNode()
- dia.LinkView - properly revert `pointer-events` attribute after a link interaction
- dia.LinkView - add root node selector for string markup
- dia.CellView - keep a dragged always view under the pointer (esp. when `restrictTranslate` in use)
- dia.CellView - make sure `cell:mouseleave` and `cell:mouseenter` events are always called when the mouse leaves/enters a cell
- dia.CellView - fix referenced bounding box for nodes outside the rotatable group
- dia.CellView - listening for underlying model changes switched from a specific attribute change (e.g. `change:size`) to a general `change` event [breaking change]
- dia.CellView - remove deprecated getStrokeBBox() [breaking change]
- dia.Cell - add generateId(), generatePortId()
- anchors - modelCenter anchor accepts `dx`, `dy` options
- linkAnchors - add anchors for link-link connections (ratio, length, perpendicular, closest)
- linkTools - add `stopPropagation` option for Vertices tool
- shapes.bpmn - add `data-flow-type` and `data-icon-type` attributes
- shapes.standard - add `standard.InscribedImage` shape
- shapes.standard - fix `itemOverflow` change and highlighting for Record
- shapes.basic - remove deprecated `PortsModelInterface` and `PortsViewInterface` [breaking change]
- util - breakText() prefers breaking words at hyphens
- util - nextFrame() extra parameters are appended to the arguments the callback receives
- Vectorizer - change `xmlns` to `svg` namespace, add correct `xmlns` namespace [breaking change]
- Vectorizer - fix translateAndAutoOrient() for edge cases
- Geometry - add divideAt() and divideAtLength() for paths
- Geometry - supports scientific notation for paths defined via SVGPath data
- Geometry - add Line.prototype.angle(), Point.prototype.chooseClosest()
- Geometry - add containsPoint() for Polyline, Path, Curve and Line
- Geometry - fix Path.prototype.closestPoint() ending in an infinite loop
- Geometry - add random()

We hope you you'll get the most from these new features, fixes and updates. Please don't hesitate to [get in touch](/cdn-cgi/l/email-protection#81eef3e6c1e2ede8e4eff5afe8ee) with questions or comments.

‍

Happy diagramming!

*- The JointJS Team*