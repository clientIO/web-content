---
source: https://www.jointjs.com/blog/rappid-21-is-now-available
generated: 2026-03-19
format: markdown
---

As we continually strive to improve JointJS+ we are very pleased to bring a new update to the world of developers. Since the release of version 2.0 we’ve been collecting your feedback, and we have now implemented a large portion of requested features which we believe will make your lives a lot easier.

“JointJS+ 2.0 brought major improvements in design and we made a lot of effort to make it easier to apply themes and more customizing. The simplified API made building diagramming applications as easy as putting Lego bricks together,” says David Durman, CEO of client IO. “Now we have taken that further by fine tuning various details of the library and adding new functionality like animated presentations and custom background image options.” he adds.

## JointJS+ 2.1 Highlights:

- Animated transitions, presentation mode
- Shape definitions are improved with custom attributes
- Custom background images for paper objects
- Rendering performance has been improved
- (JointJS TypeScript definitions)
- (JointJS+ TypeScript definitions

*Note: See complete changelog below.*

## Animations and presentation mode

Paper object now exposes new methods for focusing on elements, or any areas of your diagrams, in an animated way (zoom and translation). This is great for implementing a presentation mode in your applications.

## Customizable shape attributes

Shape definition has been simplified, and support for custom attributes has been added. This allows you to extend SVG by your own rendering logic. For example, you can set `textWrap` attribute (that does not exist in SVG) for your SVG text, and the text will automatically wrap if it’s width overflows a specified value. The `textWrap` attribute is built-in and ready-to-use, and you can also define your own custom ones.

## Custom background on each paper

It’s now possible to set a background image on your diagram paper object, define whether it should repeat or flip, or even use your own custom logic to describe how it should be displayed.

## Performance

As always when releasing a new version, in addition to adding new features and functionality we also focus on optimizing and going deeper into performance tuning. As a result you should see significant rendering improvements with JointJS+ 2.1.

## **Distribution and availability**

Users with an active JointJS+ Update Subscription can download the 2.1 update from their [Account portal](https://my.client.io). If you don't have an update subscription you can purchase it through our [online store](https://www.jointjs.com/pricing).

## Complete Changelog

### **v2.1.0 Changelog, JointJS + JointJS+:**

- update jQuery v3.1.1
- Geometry - improve Point/Rect prototype.round(precision) - fix coordinates being converted to a string after round() with a precision called, allow negative precision
- Geometry - add Rect inflate(), bottomLine(), topLine(), leftLine() and rightLine()
- Geometry - Point offset() and difference() accept both a point and x,y coordinates
- Geometry - add Line equals()
- Geometry - Line intersection() renamed to intersect() and calculates intersection points with another line or rectangle
- Vectorizer - stop accessing deprecated `nodeName` and `nodeValue` attribute properties
- Vectorizer - add prototype.contains() method
- Vectorizer - add matrixToTransformString() method as opposed to transformStringToMatrix()
- Vectorizer - add ensureId() method
- Vectorizer - add appendTo() method
- Vectorizer - V(node); does not set automatically id on the node anymore
- Vectorizer - text() with content doesn't set invalid display: null on node anymore
- Vectorizer - fix convertRectToPathData() for rounded rectangles
- dia.attributes - add namespace for defining custom attributes, allow camelCase attribute style
- dia.attributes - new attributes `sourceMarker`, `targetMarker`, `vertexMarker`, `textWrap`, `refRx`, `refRy`, `refCx`, `refCy`, `refX2`, `refY2`
- dia.attributes - improve `text` attribute performance on cellView update
- dia.attributes - fix mixing various attributes (e.g. `transform`, `refX` and `refDx` now add up)
- dia.Paper - add defineGradient(), defineFilter(), defineMarker() and isDefined() methods
- dia.Paper - fix async rendering when cell was previously member of different graph.
- dia.Paper - improve grid precision, added new grid patterns, update drawGrid() options definition.
- dia.Paper - `blank:pointerup` event is fired only after a preceeding `blank:pointerdown` event
- dia.Paper - add paperToLocalPoint(), clientToLocalPoint(), pageToLocalPoint(), localToPaperPoint(), localToPagePoint() and localToClientPoint().
- dia.Paper - add paperToLocalRect(), clientToLocalRect(), pageToLocalRect(), localToPaperRect(), localToClientRect() and localToPageRect()
- dia.Paper - add clientOffset() and pageOffset()
- dia.Cell - make cell.attr() work as getter
- dia.Cell - prop(), removeProp() accept also path defined as an array
- dia.Element - add size(), getPortPositions() methods
- dia.Element - rotate() doesn't translate embeddeded cells anymore
- dia.Link - allow arbitrary shapes for labels
- dia.LinkView - fix link translating when embedded and has no marker
- dia.LinkView - set correct port and selector on the link
- mvc.View - prevent extend() from modifying prototype propertires
- ports events `ports:add` and `ports:remove` triggered when port is added to element/removed from element
- utils - fix toggleFullScreen() in IE
- utils - breakText() takes the lineHeight style into account
- util - change cells() wrapper also accept a single cell
- highlighter.Stroke - allow multiple strokes to be applied to a single cellView magnet, prevent memory leaks
- connectors.jumpover - fix on graph `reset`

### **v2.1.0 Changelog, JointJS+ only:**

- ui.PaperScroller - add `transitionToPoint()`, `transitionToRect()`, `lock()` and `unlock()`
- ui.PaperScroller - fix autoresize in async paper mode
- ui.TextEditor: deselect text on remove
- ui.Stencil - capture pointer events for magnet=passive
- ui.Widgets - fix `toggle` change event multiple triggering
- ui.FreeTransform - add `clearAll`, `clearOnBlankPointerdown` options
- ui.Halo - add `clearOnBlankPointerdown` option
- storage.Local - fix duplicate keys in index
- add Constellation demo

We hope you enjoy these changes and updates. Please don't hesitate to [get in touch](/cdn-cgi/l/email-protection#4d223f2a0d2e2124282339632422723e382f27282e39701f2c3d3d2429687f7d7f637c637d687f7d3c38283e39242223) with questions or comments.

‍

Happy diagramming!

*- The JointJS Team*