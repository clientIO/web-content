---
source: https://www.jointjs.com/blog/why-teams-build-custom-bpmn-modeler-uis
generated: 2026-05-31
format: markdown
---

When it comes to BPMN modeling, vendor-provided solutions – e.g. Camunda Modeler or Flowable Design – may seem like the most straightforward option. You install one, open it, and start drawing processes. Why would anyone need any more than that? Well, for internal-only tooling within a small team, the convenience may be enough. However, if you are tasked with developing a workflow modeler UI for serving external customers, one that matches your product’s design language, or one that is able to do anything beyond vanilla BPMN editing, you will quickly discover that the customization options of vendor BPMN modelers are inherently unable to accommodate your application’s unique requirements.

This may be the point where we – being developers – may begin asking ourselves: *“Why don’t we build the modeler ourselves?”* (or alternatively, *“Why don’t we get an AI to make all of it for us?”*). They are both valid options to consider, of course, but as we argue in our article about the [unexpected complexity of diagramming](https://www.jointjs.com/blog/the-complexity-of-diagramming), reinventing the wheel in this case means contending with intricate issues which may not be immediately apparent to an uninitiated developer (even if they have a frontier model at their fingertips). The amount of unknown unknowns in this domain is too large, and the opportunity cost of rediscovering the problems one by one is too great.

In our opinion, getting help along the way from a mature diagramming library with BPMN support – like **JointJS** – is what tips the scale in your favor. Having the rendering, interaction, and layout diagramming foundations available out-of-the-box while still being in **complete control of everything that your users actually see and touch** hits the sweet spot between the rigidity of vendor tools and the pain of reinventing the wheel.

In previous articles in this series, we covered why BPMN modeling and execution [can be decoupled](https://www.jointjs.com/blog/bpmn-modeling-vs-execution), and what makes building a BPMN modeler [harder than it looks](https://www.jointjs.com/blog/why-building-a-bpmn-modeler-ui-is-harder-than-it-looks). Here, we will take a different angle. We will look at the **specific capabilities that a custom BPMN modeler unlocks**, and at how those can be implemented with features of JointJS.

### Note: The gap between "supported" and "useful"

Vendor-provided BPMN modelers are designed for a general audience and quick setup. To be on the safe side, they expose the BPMN 2.0 specification broadly and assume a strictly Camunda-centric (or Flowable-centric, or another-engine-centric) ecosystem. In short, they provide a one-size-fits-all editing experience.

However, being as broad as possible comes with drawbacks. In fact, providing a tailored experience is usually a requirement when the modeler is embedded in a product where branding, UX consistency, and domain specificity matter. That is where relying on a hostable library like JointJS (which can be natively embedded in your product) instead of a hosted/self-hosted monolith makes the most sense.

The features described below are areas where a diagramming library generally – and JointJS specifically – enables functionality that vendor-provided modelers fundamentally struggle to offer. Each one is a concrete reason why investing in a custom BPMN modeler UI is worth it – and each one is practical to implement thanks to JointJS's architecture.

## 1. Custom shapes: Beyond standard BPMN shapes

BPMN defines over 100 symbols, but your domain almost certainly differentiates between concepts that cannot be easily disambiguated with the standard notation alone. While all BPMN modeling interfaces need to support the entirety of BPMN standard (and most of them do), a modeler that provides *only* BPMN-standard shapes with no way to add custom ones (i.e. many vendor modelers) may force you to use the same symbol for representing multiple distinct actions, leaving your users confused. For example, while it is true that “Call backend service,” “Call external REST API,” and “Run AI pipeline” may all be appropriately represented with the same BPMN shape – `<serviceTask>` – your users may be confused why they see identical-looking boxes for three actions which work completely differently.

With JointJS, you can **ease your users’ cognitive load by defining** [**custom shape classes**](https://docs.jointjs.com/learn/features/customizing-shapes/customizing-an-existing-shape/) that extend the base BPMN elements with domain-specific markup, icons, and default properties. In the [Camunda integration demo](https://www.jointjs.com/blog/how-to-build-custom-bpmn-modeler-ui-for-camunda), for example, the HTTP Connector is a custom JointJS shape that inherits from `Activity` and carries its own default `httpConfig` (URL, method, headers, body, timeouts) alongside Camunda-specific properties like `retries` and `retryBackoff`.

-- CODE language-js --  
export class HttpConnector extends Activity {  
  defaults() {  
    return util.defaultsDeep({  
      type: 'activity.HttpConnector',  
      httpConfig: {  
        url: '',  
        method: 'GET',  
        headers: '',  
        body: '',  
        resultVariable: '',  
        connectionTimeoutInSeconds: 20,  
        readTimeoutInSeconds: 20,  
      },  
      resultExpression: '',  
      errorExpression: '',  
      retries: 3,  
      retryBackoff: 'PT0S',  
      inputMappings: [],  
      outputMappings: [],  
      attrs: {  
        icon: { iconType: 'service' },  
        label: { text: 'HTTP Request' }  
      }  
    }, super.defaults());  
  }  
}

‍`‍`The shape is visually distinct from the generic Service Task shape, carries the right icon, and – crucially – it knows what fields belong in its property panel.

**The principle is simple – each shape in your modeler needs to represent a single concept that your users understand, and each shape needs to correspond to a standard BPMN shape that other parts of the BPMN ecosystem can interface with.**

## 2. Custom canvas annotations: Visual cues for your users

When it comes to diagram annotations, vendor-provided modelers often limit themselves to the standard BPMN text annotations, which are constrained to BPMN specification’s notion of what a note looks like and how it behaves. That is, simple text boxes which are always connected to one specific diagram element. However, this may not be enough to support internal team collaboration, where different annotation styles may be required for the benefit of less-technical stakeholders, e.g. floating sticky-note comments, color-coded status labels, team assignment badges, or freeform documentation areas. Moreover, these notes are often intended purely for the design phase, and are not expected to be part of the exported BPMN XML – in those cases, the limitation of vendor-provided modelers to BPMN shapes only becomes too rigid.

Meanwhile, JointJS’s shape system treats **non-BPMN shapes as just another type of diagram element** – you can [define their shapes with arbitrary SVG or HTML markup](https://docs.jointjs.com/learn/features/customizing-shapes/creating-a-shape-from-scratch), position them freely, and decide at export time whether they should be included in the BPMN output or treated as purely visual documentation.

**The freedom to separate what the user sees from what the engine receives lets you use your own shapes wherever they make sense for you.**

## 3. Custom element palette: Curated, not overwhelming

Although supporting the entirety of BPMN 2.0 specification is a requirement for the modeler, deciding which ones to present to your users is a separate concern. After all, having all 100+ shapes in the element palette would be overwhelming for all but the most expert of power users. Although vendor modelers typically allow some shapes to be hidden, the overall structure, ordering, and visual presentation of the element palette tend to be locked down.

That is where the programmability of JointJS’s [**Stencil component**](https://docs.jointjs.com/learn/features/element-palette) offers a solution. It allows you to decide which shapes (whether standard BPMN shapes, custom shapes, or non-BPMN annotations) should appear in the palette – and how they should be grouped, labeled, and previewed for your users. For instance, if your company’s workflows only use a limited subset of BPMN (or if you are [limited by your execution engine](https://docs.camunda.io/docs/components/modeler/bpmn/bpmn-coverage/)), making only those elements available in the palette is a good idea.

**Curating the element palette makes your modeling interface approachable for your users, and it ensures the validity of the generated diagrams for your domain.**

## 4. Dynamic property editor and viewer: Two-way binding for your data

Although the property panel is not visible at first glance, do not make the mistake of overlooking its importance! Your users will spend a considerable amount of time interacting with it to set up BPMN correctly for execution engines, and so being able to set it up as your users need is crucial. This is where vendor modelers fall short – their one-size-fits-all approach of fixed property panels (the same fields in the same order for every instance of a given shape) fails to take into account who the user is or what is happening in the diagram.

JointJS addresses these limitations with its [**Inspector component**](https://docs.jointjs.com/learn/features/property-editor-and-viewer), which is easily customizable via serializable JS objects. A single configuration object allows you to control the grouping, ordering, conditional visibility (e.g. show the “Error Code” field only when the event type is “Error”) and input validation of form fields according to your selection. This makes it possible to define a separate dynamic property panel layout for each shape in your diagram – in the [Camunda integration demo](https://www.jointjs.com/blog/how-to-build-custom-bpmn-modeler-ui-for-camunda), it allowed us to set up the HTTP Connector’s inspector panel so that it presents grouped fields for HTTP configuration, timeouts, retries, and I/O mappings (all different from the fields shown for the generic Service Task). The Inspector constructs the HTML form as directed and maintains a two-way data-binding between it and the diagram, ensuring that the property panel is always synced with the state of the diagram and refreshed if necessary.

**Dynamic property panels allow you to support intuitive interaction scenarios that make it easy for your users to configure their BPMN objects.**

## 5. Custom UI event handlers: Interaction that is application-specific

Vendor modelers give you the interaction model they decided on. If you want double-click to open an inline editor, or right-click to show a context menu with deployment options, or shift-drag to initiate a bulk selection – you can only do it if the vendor chose to support that interaction.

However, chances are that the vendor’s decisions do not exactly match your requirements. JointJS provides a **rich event system** that exposes granular [pointer and touch events](https://docs.jointjs.com/learn/features/diagram-basics/events/) for every element, link and port on the canvas, and [keyboard events](https://docs.jointjs.com/learn/features/keyboard-shortcuts) for custom shortcuts. You can set up your own behaviors for element right-click, link double-click, port hover, CTRL-ALT-0, and nearly anything else you can think of. At the same time, JointJS also allows you to call `preventDefaultInteraction()` on the event target to suppress JointJS’s default event behavior and substitute your own. This gives you building blocks to implement exactly the interaction model your specific users need – so that a tool aimed at BPMN experts can embrace keyboard shortcuts for efficiency, while a tool aimed at BPMN novices can prioritize mouse interactions with plenty of hovering tooltips and nested context menus.

**Sensible defaults are important – but being able to add, change, or remove interactions as needed for your specific use case gives you the freedom to delight your users.**

## 6. Automatic layouts: Keeping things organized

Vendor-provided BPMN modelers typically offer no automatic layout functionality at all, or at best a single rigid “auto-arrange” button that repositions everything into a fixed hierarchy. Users are expected to manually place and align every element – which may be fine for small diagrams, but becomes a significant friction point as the number of interconnected tasks grows. The lack of layout automation means that users have to spend time on visual housekeeping instead of the workflow logic they are trying to model.

JointJS provides a suite of [**automatic layout algorithms**](https://docs.jointjs.com/learn/features/automatic-layouts/) that can be applied programmatically (e.g. when the user presses a button) to the entire graph or to a selected subset of elements, including general-purpose `DirectedGraph` (powered by Dagre) and `MSAGL`; `TreeLayout`, `GridLayout` and `StackLayout` for structured arrangements; and `ForceDirected` for loosely structured graphs. Alternatively, instead of triggering this activity on demand, you may let the layout algorithm handle all positioning and disable free drag-and-drop, and turn your modeler into a connect-the-steps experience for your users.

**Automatic layouts reduce the skill floor for your modeler UI – even users who have never drawn a BPMN diagram can produce clean, readable processes on their first try.**

## 7. Custom execution visualization: Highlighters for your data

Once a process is deployed and running, your users will want to see if it is running as expected. Vendor platforms handle this in separate monitoring dashboards (Camunda Operate, for example), but that means context-switching away from the modeler, which is not ideal.

In simple situations (e.g. a single deployment of a BPMN diagram, a single execution of a deployment), it may be enough to visualize execution state directly on the process diagram (both real-time token animation and persistent status information), which is where JointJS’s [**extensible highlighter system**](https://docs.jointjs.com/learn/features/highlighters/) comes in handy. Highlighters are views that add visual emphasis to any element or sub-element on the canvas, and they can be manipulated programmatically in response to external information (which may come from querying your execution engine’s REST API, or from any other data source). Built-in highlighters include `mask` (which adds a stroke around a shape), `opacity` (which adjusts shape transparency), `addClass` (which toggles a CSS class), and `list` (which renders custom SVG elements), and it is also possible to implement your own custom highlighters. These can be activated on demand and composed as necessary – for example, to track the execution status of your process, you could: add a green stroke around an active task, reduce opacity for all completed tasks, and attach an error badge for any failed ones. Alternatively, highlighters can be used to display persistent status information based on `extensionElements` or custom metadata on shapes (e.g. validation warnings, completed instance counts, SLA compliance indicators).

**Vendor-provided solutions typically enforce strict separation between modeling and monitoring UIs, but for simple situations this adds unnecessary overhead. Being able to communicate execution information directly in the diagram lets you design the execution status interfaces around the information your users care about, in the visual language they already understand from the rest of your product.**

## Other areas where JointJS delivers unique value

The features above are the most prominent differentiators, but the advantages of a custom modeler built with JointJS extend further:

- **Virtual rendering for large diagrams.** JointJS dynamically renders only the SVG elements visible in the user's viewport, which means diagrams with hundreds of elements remain performant. This is a [limitation](https://forum.camunda.io/t/bpmn-modeler-performance-issues-with-large-diagrams/58520) of alternatives like Camunda Modeler, which do not implement virtual rendering.
- **Touch and mobile support.** JointJS includes touch interaction out-of-the-box, which matters for tablet-based use cases. (Notably, bpmn-js explicitly removed out-of-the-box touch interaction support [in a recent release](https://bpmn.io/blog/posts/2024-bpmn-js-17-removing-touch-interaction-support.html).)
- **Framework-agnostic integration.** JointJS works with [React, Angular, Vue, Svelte, and plain TypeScript](https://docs.jointjs.com/learn/integration/) – the modeler can be embedded wherever your product lives.
- **Compatibility with any BPMN engine.** Vendor-provided modelers are tightly coupled to a specific execution engine (Camunda, Flowable, etc.), so switching providers may be difficult down the line. JointJS allows you to decouple your data and its representation in engine-specific extensions, which lets you adapt to changing conditions.
- **Custom validation rules.** Because JointJS is engine-agnostic, you define your own validation logic. This means you can enforce not just BPMN structural rules and engine-specific requirements, but also organization-specific business rules that no vendor modeler could anticipate.
- **Bidirectional BPMN 2.0 XML import/export.** JointJS's toBPMN() and fromBPMN() functions handle the standard BPMN 2.0 schema, and the export pipeline can be post-processed to inject engine-specific extensions – as demonstrated in the [Camunda integration tutorial](https://www.jointjs.com/blog/how-to-build-custom-bpmn-modeler-ui-for-camunda).**‍**
- **Extensibility beyond BPMN.** BPMN support is only a subset of the functionality of JointJS. The framework features you would use to create a custom BPMN modeler UI (diagram functionality, element palette, property editor and viewer, highlighters, undo/redo, snaplines, selection, etc.) are the same ones you would use to create a workflow designer, a network architecture diagram, or another kind of modeler (e.g. DMN, CMMN, ArchiMate,...). The JointJS demo page has [many boilerplate applications](https://www.jointjs.com/demos?tags=Boilerplate+applications) you can use as the starting point on your journey.

## When is the investment worth it?

Not every team needs a custom BPMN modeler. If you are building internal tooling for a small team of BPMN experts, and your chosen engine’s modeler covers your requirements, then the vendor solution is probably the right call. **The investment in a custom modeler pays off when one or more of the following conditions are true:**

- The modeler is part of a **customer-facing product** where branding, UX consistency, and domain-specific guidance matter.
- Your users are **not BPMN experts**, and you need to ease their cognitive load with custom shapes, element palette curation, intuitive property panels, and automatic layouts.
- Your users expect specific **interaction modes** like complex keyboard shortcuts or touch support.
- You need to **visualize execution state** within the same interface where processes are designed, rather than requiring users to switch between separate tools.
- Your diagrams are large enough that **rendering performance** becomes a concern – typically above a few hundred elements.
- The modeling UI needs to support **other diagramming** on top of BPMN as well.

In each of these cases, JointJS provides the foundation that lets your team focus on the domain-specific layer – shapes, user interaction, and engine integration – rather than reinventing diagramming functionality from scratch.

## Summary

Vendor-provided BPMN modelers are convenient starting points, but they impose constraints that become increasingly painful as your product matures. Custom BPMN modeler UIs – built on a capable diagramming foundation like JointJS – unlock specific capabilities that vendor tools cannot match: **Custom shapes and annotations, curated element palettes, dynamic property editors, tailored interaction models, automatic layouts, and rich execution status displays**.

If you want to see what a JointJS-based BPMN modeler looks like in practice, the [**BPMN Editor demo**](https://www.jointjs.com/demos/bpmn-editor) provides a production-oriented starting point, and the [**Camunda integration tutorial**](https://www.jointjs.com/blog/how-to-build-custom-bpmn-modeler-ui-for-camunda) walks through connecting it to a real execution engine. Between the two, you can go from zero to a fully functional custom modeler – with domain-specific shapes, an engine-aware property panel, and deployment from the toolbar – in days rather than months.**‍**

**Happy diagramming!**

**‍**

## **FAQs**

Why would I build a custom BPMN modeler instead of using a vendor-provided one like Camunda Modeler or Flowable Design?

What specific limitations do vendor-provided BPMN modelers have?

Is building a custom BPMN modeler from scratch realistic, or is it too much work?

When is the investment in a custom modeler actually worth it?

How can I handle domain-specific concepts that all map to the same BPMN shape?

Can I add non-BPMN visual elements to a BPMN diagram, and what happens to them on export?

Can I visualize the process execution state directly in the modeler?

Are there any automatic layout options which would help non-expert users produce clean BPMN diagrams?

What is the performance of a custom BPMN modeler with large diagrams?