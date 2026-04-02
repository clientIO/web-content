---
source: https://www.jointjs.com/blog/link-teleports
generated: 2026-04-02
format: markdown
---

In complex, production‑grade diagrams, the network of interconnected paths can quickly become so dense that following the flow and understanding its logic becomes difficult.

The most common issues you'll encounter in business-critical workflows:

- Connected nodes no longer fit on a single screen, forcing users to zoom out so far that labels and annotations become unreadable.
- Path lines overlap and intertwine, making it difficult to follow the flow and understand the underlying logic.

The concept of Link Teleports directly addresses these issues by replacing tangled connections with compact, clickable markers. This keeps the canvas visually clean while preserving — and often improving — clarity about which elements are connected.

## What we'll build: Dynamic, UI-driven Link Teleports

In this guide, we'll implement Link Teleports in a JointJS application using two distinct UI patterns:

1. **Dynamic distance-based behavior** — links automatically switch between standard paths and teleport markers based on the distance between connected elements.
2. **Toggle-based behavior** — a UI toggle switch that allows users to flip between standard paths and teleport markers on demand.

By the end, you'll have two practical implementation patterns that you can adopt for your flow diagrams to significantly improve the usability of your application.

## How to set up dynamic, distance-based Link Teleports in JointJS

The dynamic, distance-based approach adjusts the UI automatically based on the distance between connected elements. When a connection exceeds a predefined threshold, the standard path is replaced with a Link Teleport.

This gives your application a hybrid of standard links and Link Teleports. Where it makes sense, paths remain fully drawn to connect nearby nodes, but once they become visually disconnected, the UI seamlessly switches to Link Teleports.

### Implementing a distance-aware `defaultConnector`

The core of the distance-based approach is overriding the default connector between links.

In the `paper` initialization, we override the `defaultConnector` and conditionally replace standard connector paths if the distance between elements exceeds the configured value in the `MIN_DISTANCE` constant.`‍`‍

New connector logic:

```
const paper = new dia.Paper({
  // ...
  defaultConnector(sourcePoint, targetPoint, routePoints, _, linkView) {

    const distance = /* calculate distance between elements */;

    if (distance > MIN_DISTANCE) {
      // Return a short path segment near the source/target,
      // with its size defined in the SEGMENT_LENGTH constant
    } else {
      // Return a normal connected path
    }
  }
});
```

Note that we’re changing the connector type based on the distance between elements; `MIN_DISTANCE` is the threshold that determines when a standard path should be replaced by Link Teleports.

The complete `paper` initialization with configuration constants:

```
// Determine the length of the new endpoints.
const SEGMENT_LENGTH = 50;

// Determine the minimum distance required to trigger dynamic Link Teleports 
const MIN_DISTANCE = 600;

const paper = new dia.Paper({
    gridSize: 10,
    drawGrid: true,
    model: graph,
    defaultAnchor: {
        name: 'midSide',
        args: {
            useModelGeometry: true,
            mode: 'prefer-horizontal'
        }
    },
    defaultConnectionPoint: {
        name: 'anchor'
    },
    defaultRouter: {
        name: 'rightAngle'
    },
    // Override the default connector to create gaps in the link when the
    // distance between the connected elements is large enough.
    defaultConnector: function(
        sourcePoint,
        targetPoint,
        routePoints,
        _,
        linkView
    ) {
        const sourceCenter = this.sourceView.model.getCenter();
        const targetCenter = this.targetView.model.getCenter();
        const distance = sourceCenter.distance(targetCenter);
        if (distance > MIN_DISTANCE) {
            const path = new g.Path();
            const sourceEndPoint = sourcePoint
                .clone()
                .move(sourceCenter, SEGMENT_LENGTH);
            path.appendSegment(g.Path.createSegment('M', sourcePoint));
            path.appendSegment(g.Path.createSegment('L', sourceEndPoint));
            const targetStartPoint = targetPoint
                .clone()
                .move(targetCenter, SEGMENT_LENGTH);
            path.appendSegment(g.Path.createSegment('M', targetStartPoint));
            path.appendSegment(g.Path.createSegment('L', targetPoint));
            return path;
        }
        return connectors.straight(sourcePoint, targetPoint, routePoints, {
            cornerType: 'cubic',
            cornerRadius: 10
        });
    }
});
```

## Implementing Link Teleport markers

The visual markers for Link Teleports are implemented as custom buttons that extend JointJS built-in link tools. Each link receives two markers: one positioned near the source element and one near the target.

There are two key aspects to the button configuration: **visibility** and **action**.

**Visibility** — a marker is only rendered when the distance between connected elements exceeds `MIN_DISTANCE:`

```
visibility(view) {
  const distance = /* calculate distance */;
  return distance > MIN_DISTANCE;
}
```

`‍`**Action** — clicking a marker scrolls the paper to the corresponding connected element:`‍`

```
action(evt, linkView) {
  // For the source marker: scroll to the source element
  // For the target marker: scroll to the target element
  paper.scrollToElement(element);
}
```

The snippets above are simplified for readability. In a production implementation, the button action would typically emit a custom event, with the actual scrolling logic handled by dedicated event listeners.

`‍`The full Link Teleport buttons implementation:`‍`

```
// Link Teleport Buttons
function getTeleportButtonMarkup(text) {
    return [
        {
            tagName: 'rect',
            selector: 'button',
            className: 'teleport-button',
            attributes: {
                x: -30,
                y: -10,
                width: 60,
                height: 20,
                rx: 5,
                ry: 5,
                fill: '#9CE8B8',
                stroke: '#33334F',
                strokeWidth: 1,
                cursor: 'pointer'
            }
        },
        {
            tagName: 'text',
            selector: 'label',
            textContent: text,
            attributes: {
                x: 0,
                textAnchor: 'middle',
                dominantBaseline: 'central',
                fill: '#33334F',
                fontSize: 10,
                fontFamily: 'sans-serif',
                pointerEvents: 'none'
            }
        }
    ];
}

// Helper function to determine distance between elements
function getEndDistance(link) {
    const sourceCenter = link.getSourceElement().getCenter();
    const targetCenter = link.getTargetElement().getCenter();
    return sourceCenter.distance(targetCenter);
}

// The teleport button
const TeleportButton = linkTools.Button.extend({
    name: 'teleport',
    options: {
        // end: 'source' | 'target'
        distance: function() {
            return this.isAtSource() ? -SEGMENT_LENGTH : SEGMENT_LENGTH;
        },
        markup: getTeleportButtonMarkup('Teleport'),
        visibility: (view) => getEndDistance(view.model) > MIN_DISTANCE,
        action: (evt, view, tool) => {
            const end = tool.options.end;
            view.notify(`teleport:${end}`, evt);
        }
    },
    isAtSource() {
        return this.options.end === 'source';
    },
    update() {
        linkTools.Button.prototype.update.apply(this, arguments);
        const link = this.relatedView.model;
        const endElement = this.isAtSource()
            ? link.getSourceElement()
            : link.getTargetElement();
        this.childNodes.label.textContent = `${endElement.attr('label/text')}`;
    }
});

// Link Teleports Interaction / Even Handling
paper.on('teleport:source', (linkView) => {
 paperScroller.scrollToElement(linkView.model.getSourceElement(), {
        animation: true
    });
});

paper.on('teleport:target', (linkView) => {
    paperScroller.scrollToElement(linkView.model.getTargetElement(), {
        animation: true
    });
});
```

The final step is to attach Teleport Buttons to each link. We will iterate over all links and initialize the buttons—the visibility of the buttons is then, as shown before, determined in the `visiblity()` callback function of the extended button configuration.

```
// Add link teleport buttons to each link
graph.getLinks().forEach((link) => {
    const linkView = link.findView(paper);
    linkView.addTools(
        new dia.ToolsView({
            tools: [
                new TeleportButton({ end: 'source' }),
                new TeleportButton({ end: 'target' })
            ]
        })
    );
});
```

### `‍`Demo: Dynamic, distance-based Link Teleports in action

We now have fully working, dynamic Link Teleports that automatically switch from standard connectors to teleport markers when the distance between nodes crosses the configured threshold.

Explore the dynamic, distance-based Link Teleports behavior in the live demo: <https://www.jointjs.com/demos/link-teleports>

## How to set up toggle-based Link Teleports in JointJS

The distance-based approach to Link Teleports works automatically, but there are cases where you’ll want to give users explicit control. In this section, we’ll add a UI toggle that lets users switch between standard connector paths and Link Teleports on demand.

The underlying setup is similar to the dynamic, distance-based implementation described earlier. The key difference is the condition that determines when Link Teleports are shown or hidden: instead of relying on the distance between elements, the behavior is now driven entirely by state.

### Tracking the UI toggle state

We'll store the current state of Link Teleports on the `graph` itself, so it's accessible anywhere you have a reference to the graph.

```
graph.set('teleportMode', false);
```

By default we use standard paths, so `teleportMode` is initialized to `false`.

Next, we'll add a toolbar toggle switch using the built-in `ui.Toolbar`:`‍`‍

```
const toolbar = new ui.Toolbar({
    theme: 'modern',
    tools: [
        {
            type: 'toggle',
            name: 'teleportMode',
            label: 'Teleport Mode',
            value: graph.get('teleportMode'),
        }
    ]
});
document.getElementById('toolbar-container').appendChild(toolbar.el);
toolbar.render();
```

Finally, we’ll also need a corresponding container element for the toolbar in the HTML:

```
<div id="toolbar-container"></div>
```

### Updating connector and visibility logic

Instead of checking `MIN_DISTANCE`, both the `defaultConnector` and the marker `visibility` function now use the `teleportMode` state:

```
// In defaultConnector:
if (linkView.paper.model.get('teleportMode')) { ... }

// In TeleportButton:
visibility: (view) => view.paper.model.get('teleportMode')
```

With these two changes, the *Link Teleports* can be enabled or disabled based on the current `teleportMode` state. The final step is to add an event listener to the toolbar to update this state and refresh the diagram when the UI control is toggled.`‍`

```
toolbar.on('teleportMode:change', (value) => {
    graph.set('teleportMode', value);
    graph.getLinks().forEach(link => {
        const view = link.findView(paper);
        view.requestConnectionUpdate()
    });
});
```

When the user flips the toggle, we’ll change the state and call `requestConnectedLinksUpdate()` to force JointJS to re-render the links on canvas, switching between standard paths and Link Teleports as needed.

### `‍`Demo: Toggle-based Link Teleports

With the toggle in place, switching the control instantly changes how the entire diagram is rendered. In teleport mode, every long-distance connection gets replaced by markers; switch it off, and the standard paths are restored.

On a small diagram with only a few elements, the effect may seem subtle. But once you have a complex, real-world diagram with many elements on the canvas, the difference becomes clear. Link Teleports remove visual noise and make the diagram flow much easier to understand.

Explore the toggle-based Link Teleports behavior in the live demo: <https://changelog.jointjs.com/gallery/link-teleports-toggle-ui/>

## When to use each approach

**Distance-based behavior** is a strong default for general-purpose diagrams where elements are frequently repositioned. The diagram adapts automatically as the layout changes.

**Toggle-based behavior** is better suited to scenarios where the diagram has a relatively stable density and automatic switching might feel inconsistent or unpredictable.

In some cases, you'll get the best results by combining both behaviors: use distance-based Link Teleports as the default, while still exposing a UI toggle so expert users can override the behavior when they need explicit control.

## Conclusion

Link Teleports are one of those features that feel like a small refinement until your diagrams reach real-world complexity. Once you start working with flows that scale beyond a handful of nodes, they quickly become difficult to navigate without this kind of UI pattern.

If you're already experimenting with Link Teleports in your application, or if you have questions about adapting the patterns in this guide to your own use case, feel free to reach out—we’d be happy to hear from you.

Happy diagramming!

‍

‍

## FAQs

What are Link Teleports?

Why should I use Link Teleports in complex diagrams?

How do Link Teleports work conceptually?

What are the two main Link Teleport patterns?

How does the dynamic, distance-based Link Teleport mode work?

What are the implementation details of Link Teleports in JointJS?

What happens when a user clicks a teleport marker?

How does the toggle-based Link Teleports mode differ from the distance-based one?

When should I use which Link Teleports UI pattern?

Where can I see Link Teleports in action?