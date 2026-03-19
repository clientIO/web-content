---
source: https://www.jointjs.com/blog/rappid-2-4-has-arrived
generated: 2026-03-18
format: markdown
---

JointJS+ 2.4 is now available and brings along some great updates, fixes, and cool new features. We're especially excited to release two completely new demos which demonstrate how to truly integrate JointJS+ with Angular and React.

> *"Although it's already been possible to integrate Angular and React with JointJS+, many users didn't understand how to do it." says David Durman, CEO of client IO. "With these new demos, which are free to use and include source code, devs can easily explore the integration logic for use in their own solutions."*

In addition to the demos we have improved many popular widgets with some great new features. It's definitely worth checking out!

You can download the update package from your [Account portal](https://my.client.io). If you're not eligible for a free update you can purchase it through our [online store](https://www.jointjs.com/pricing) or request a free [30 day trial](https://www.jointjs.com/free-trial) to try it out.

Take a look at the main highlights here and the full changelog below.

## JointJS+ 2.4 Highlights:

### New Shapes for displaying and mapping structured data

- Record, Bordered Record and Headered Record for displaying structured data
- Hide Fill Boundaries, Show Right Fill Boundary, Fill Padding, and ticks option for y axis for Plot charts
- Add a background to BorderedImage

‍

### Angular and React integration

- KitchenSink applications now integrated with Angular6 and React
- <https://www.jointjs.com/demos/kitchen-sink-app>

‍

### Plenty of improvements to the current widgets

- Paper now supports relative dimensions (e.g. width = 100%)
- Paper introduces new interactions and settings
- Improved touch interactions
- Other improvements in Inspector, Stencil, Graph, Paper, Print, shapes and utils

### Two brand new demos including source code

- Data Mapping: <https://www.jointjs.com/demos/data-mapping>
- Combined Tree with Grid Layout: <https://www.jointjs.com/demos/jointjs-layouts>

‍

## Complete JointJS+ v2.4 Changelog:

- add DataMapping & Layout applications
- add KitchenSink applications integrated with Angular6 and React
- ui.ContextToolbar - add vertical option
- ui.Inspector - add renderLabel() option
- ui.Inspector - add max and min options for lists
- ui.Inspector - options callbacks (validateInput, renderFieldContent, getFieldValue) now receive the inspector reference
- ui.Inspector - fix nested lists issues and create() method when a cellView was passed
- ui.Inspector - enable editing arbitrary Backbone.Model
- ui.Stencil - allow custom element views for cells (in the stencil and while dragging)
- ui.Toolbar - fix actions being triggered twice on touch devices
- ui.PathDrawer - add snapRadius options
- format.Print - improve cross-browsers printing
- dia.Graph - getCellsBBox() takes cells' rotation into account
- dia.Graph - fix cell removal after dry flag passed
- dia.Paper - support relative dimensions (e.g. width='100%')
- dia.Paper - add stopDelegation interactive option
- dia.Paper - add magnetThreshold option (create a link when the pointer leaves the magnet)
- dia.Paper - allow to stop propagation of paper events
- dia.Element - add removePorts()
- dia.ElementView - add element:magnet:pointerclick, element:magnet:dblpointerclick, element:magnet:contextmenu events
- dia.ElementView - fix embeddingMode for Lodash v4+
- dia.ElementView - fix cell:pointerclick in Chrome after DOM change
- dia.LinkView - prevent multiple validate connections for already snapped magnets
- dia.LinkView - fix label rendering in IE
- dia.Cell - JSON Markup accepts textContent and groupSelector properties
- dia.CellView - presentation attributes (attrs) are now applied in the given order
- mvc.View - prevent multiple onRender() calls
- mvc.View - add findAttribute()
- mvc.View - prevent className undefined
- dia.attributes - add ellipsis option for textWrap
- dia.atributes - add refWidth2 and refHeight2
- shapes.standard - add Record, BorderedRecord and HeaderedRecord for displaying structured data
- shapes.charts - add hideFillBoundaries, showRightFillBoundary, fillPadding, ticks option for y axis for Plot charts
- shapes.bpmn: fix text position for Activity shape in IE
- shapes.standard - add background to BorderedImage
- shapes.standard - add InscribedImage shape
- shapes.pn - fix PlaceView
- connectionPoints.Boundary - fix for non-graphical elements
- routers.manhattan - prevent rounding errors, add padding option
- routers.orthogonal - add padding option
- utils - normalize event.target in normalizeEvent() for <use> tag in IE
- utils - improve parseCssNumeric() for restrictUnit parameter
- Vectorizer - add isSVGGraphicsElement()
- fix touch interactions
- fix legacy PortsViewInterface
- various Typescript fixes
- refer canvg dependency by a version instead of tarball URL

We hope you you'll get the most from these new features, fixes and updates. Please don't hesitate to [get in touch](/cdn-cgi/l/email-protection#94fbe6f3d4f7f8fdf1fae0bafdfb) with questions or comments.

‍

Happy diagramming!

*- The JointJS Team*