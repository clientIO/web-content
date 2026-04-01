---
source: https://www.jointjs.com/blog/introducing-version-4
generated: 2026-04-01
format: markdown
---

**We're excited to announce v4.0 of JointJS and JointJS+, the first no-dependency edition of our diagramming library!** 🎉 We've listened to your feedback and concerns and have finally launched a stable version that does not use *jQuery*, *Backbone*, and *Lodash*. Among other benefits, this update makes our library leaner without changing the core functionality.

The latest release brings more improvements, and we will briefly go through them in this blog post. If you want to dig into all the technical details of this release, we encourage you to [read the full changelog.](https://docs.jointjs.com/releases/changelogs/4.0.0)

*"Version 4.0 is a milestone we have all been waiting for. We were aware of the counterintuitive parts of our code base and the dependency on legacy libraries—the latest version addresses these issues. We refined the API to improve onboarding and eliminated external dependencies to enhance performance and gain complete control over our library," adds Roman Brückner, the company's CTO.*

⚠️ **Important**: Version 4.0 introduces breaking changes. Therefore, JointJS+ customers should [read the migration guide](https://docs.jointjs.com/releases/changelogs/4.0.0) from 3.7 to 4.0 to ensure smooth transition to the latest version.

### Stable version with no external dependencies

As stated earlier, we now introduce a dependency-free edition that does not rely on *jQuery*, *Lodash*, and *Backbone*. This long-awaited improvement makes our library leaner (decreases the package size as demonstrated below) and empowers us to fully control the core functionality, and make adjustments to our customers' specific needs. The level of customizability of JointJS and JointJS+ is one of our prides, and version 4.0 enables us (and you) to adjust the library without making any compromise.

Let's sum up the key benefits of this update:

- **Full control over the library:** We're now in charge of the entire code base and are fully responsible and capable of fixing any bug reported by our customers. The same possibilities apply to our community, which helps us improve [JointJS, our open-source edition](https://github.com/clientIO/joint).
- **Leaner and high-performing:** By relying on external dependencies built to serve many different use cases, we included lots of unnecessary functionality in our code base. This has now changed, improving performance and giving us the ability to tailor our library to any specific use case.
- **Significant upgrade with smooth migration:** We've preserved more than 90% of the API functionality and have done everything to make your migration from previous versions smooth. Although JointJS and JointJS+ now feel like a new library, the change does not require any learning effort on your part and comes with a [very straightforward migration process](https://docs.jointjs.com/releases/changelogs/4.0.0).

On the topic of the decreased package size, below is a visual example illustrating the structure of a simple visual application built with JointJS. Before version 4.0, the total size of the application, including external JointJS dependencies, was 1.94MB. With the release of version 4.0, the application size was reduced to 1.1MB, achieving a 44% improvement.

### BPMN export to/import from XML format

BPMN, standing for Business Process Model and Notation, is a standardized modeling language and notation system extensively utilized by corporations to graphically depict their business processes. It enables companies to document, analyze, and optimize their workflows in a comprehensive manner. BPMN models can be serialized into an XML format, known as BPMN XML, facilitating the easy exchange and storage of business process diagrams across various BPMN-compliant tools, such as BPMN editors and automation engines. **In JointJS+ 4.0, a BPMN diagram can be seamlessly imported from or exported to XML, enhancing collaboration across the entire BPMN tool suite.**

See how simple it is to export a process designed in our [BPMN editor](https://www.jointjs.com/demos/bpmn) and import it into [Camunda](https://camunda.com/) for end-to-end process automation.

### Extensive refactoring for improved performance

We have eliminated obsolete code, aiming not only to enhance performance but also to make your interaction with our codebase more intuitive. Debugging becomes easier with improved error messaging; all diagrams are, by default, faster and visually more appealing. Moreover, specific parts of the package were separated, further reducing the package size. This is evident in the case of shapes that can still be copied from our examples and used in your project but are not included in the package.

Additionally, with version 4.0, we are taking another significant step towards becoming a fully modular diagramming library and building an ecosystem that benefits from our core functionalities and other widely used technologies. The result will be a plethora of advanced features in the form of modules that combine the strengths of our core functionality and other technologies such as [D3](https://d3js.org/), [Cytoscape](https://cytoscape.org/), or [Graphviz](https://graphviz.org/) and can optionally be used in your project but are not part of the JointJS and JointJS+ core by default. In our backlog ([feel free to add your ideas on what to do next, by the way](https://github.com/clientIO/joint/discussions/categories/ideas)), there are lots of useful features that you can expect in the upcoming weeks! 🙌

### New demo: Image Processor

The source code of a recently published demo application, the Image Processor, is now part of the JointJS+ package, helping you to copy and paste our work and reuse it for your own project as a boilerplate. The Image Processor application enables you to manipulate images using filters and transformation tools in a node-based manner. To access the source code, download the latest version of JointJS+ in [our customer portal](https://my.jointjs.com/), or [start a free trial](/free-trial).

### Other changes

- [NEW FEATURE] Grid now renders as an SVG document inside the paper (not HTML) and can be rendered in the exported SVG, PNG or on the print page
- [NEW FEATURE] Several enhancements have been made to paper transformations, such as triggering higher-level events, passing custom data along with the events, and simplify scaling at point method
- [NEW FEATURE] Camel-case attributes are supported across the entire framework
- [ONBOARDING] Improved error messaging for easier debugging
- [REFACTORING] Sensible defaults have been set to ensure that you work with visually pleasing and high-performing diagrams from the start
- [PERFORMANCE] Evaluation of calc expressions and SVG attribute names are set at the core, enabling more efficient updates to DOM elements
- [BUG FIX] SVG filters work with links now

#### **Next steps?**

You can get a complete overview of what's new by [reading our full changelog](https://docs.jointjs.com/releases/changelogs/4.0.0). If you're ready to start building with JointJS+ 4.0, choose one of these paths:

- JointJS+ customers can download the latest package in [our customer portal](https://my.jointjs.com/) (read the [migration guide](https://docs.jointjs.com/releases/changelogs/4.0.0) for a smooth transition from 3.7).
- Non-customers can [start a free 30-day trial](/free-trial) to access the latest features and improvements and evaluate JointJS+ for their project.

**Excited to shape the future of diagramming with us?** [Share your ideas for new features and improvements on our GitHub](https://github.com/clientIO/joint/discussions/categories/ideas) and influence what the next JointJS and JointJS+ versions will look like.

‍

Happy diagramming!