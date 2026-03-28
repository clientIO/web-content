---
source: https://www.jointjs.com/blog/rappid-v16-prague-released
generated: 2026-03-28
format: markdown
---

The new **JointJS+** doesn't just improve the current set of components, it adds a lot of new ones, too. Now you can create truly advanced flow chart editors, network monitoring systems, workflow tools and other diagramming applications in days.

## New features

### Rich-text support in inline Text Editor

The JointJS+ **ui.TextEditor** component for inline editing of texts in diagram elements and links went through another heavy development iteration. The new version adds support for rich-text editing and improves the API with a syntactic sugar for much easier setup of inline editing. See the [docs](https://resources.jointjs.com/docs/rappid/v3.5/ui.TextEditor.html) for more details.

### Flash Messages

[Flash messages](https://resources.jointjs.com/docs/rappid/v3.1/ui.html#ui.FlashMessage) are great for quickly informing the user that something has happened without worrying about the state of the UI. Just throw a flash message and let the widget worry about destroying itself and cascading one on top of another.

### Dropdowns

[ui.SelectBox](https://resources.jointjs.com/docs/rappid/v3.5/ui.SelectBox.html) widget gives you a full-featured dropdowns with arbitrary HTML content, built-in support for icons, different open policies and keyboard navigation.

### Select Button Groups

Use [ui.SelectButtonGroup](https://resources.jointjs.com/docs/rappid/v3.5/ui.SelectButtonGroup.html) component to display groups of buttons with both single and multi selection support.

### Color Palette

[ui.ColorPalette](https://resources.jointjs.com/docs/rappid/v3.5/ui.ColorPalette.html) is a perfect component for color selection. Instead of using the browser native color picker which does not work in all browsers, take control of color selection for your shapes with a pre-designed set of colors.

### New Halo Control Panel Types

The [ui.Halo](https://resources.jointjs.com/docs/rappid/v3.5/ui.Halo.html) control panel widget was extended with two more types as an alternative to the current version with icon tools surrounding the selected element. The two new types are *toolbar* and *pie* menu. You can switch between types just by setting the type option.

### Lightbox

[ui.Lightbox](https://resources.jointjs.com/docs/rappid/v3.5/ui.Lightbox.html) makes it easy to display images in a popup that fills the screen and dims out the rest of the application. The lightbox automatically adjusts its size based on the size of the screen.

## ... and more!

The [JointJS Core API](https://resources.jointjs.com/docs/jointjs/v3.6/joint.html) was extended by tons of new methods and current methods were improved too. Just to name a few: [Vectorizer](https://resources.jointjs.com/docs/jointjs/v3.6/vectorizer.html), the SVG mini-library that is part of JointJS, was extended with methods to convert SVG shapes to SVG paths. Also, the text()method can now render rich-text. [dia.Paper](https://resources.jointjs.com/docs/jointjs/v3.6/joint.html#joint.dia.Paper) has a new, awaited, option for disabling links that do not have source or target (links pinned to the paper). Many of the JointJS+ widgets were improved as well. [ui.FreeTransform](https://resources.jointjs.com/docs/rappid/v3.5/ui.FreeTransform.html) now accepts preserveAspectRatio option for preserving the aspect ratio. [ui.Inspector](https://resources.jointjs.com/docs/rappid/v3.5/ui.Inspector.html) property editor contains three new types (select-box, select-button-group and color-palette) as well as methods that make it easy to add custom fields. And the list goes on and on... See the JointJS+ v1.6 Prague CHANGELOG page for full details.

[BUY JOINTJS+ AND BUILD GREAT APPS NOW!](https://www.jointjs.com/jointjs-plus)

If you missed our previous release, visit our blog post to see what components were added and which ones were improved in [JointJS+ v1.5 Amsterdam](https://www.jointjs.com/blog/rappid-v15-amsterdam-released).