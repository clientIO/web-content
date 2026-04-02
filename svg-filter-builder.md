---
source: https://www.jointjs.com/blog/svg-filter-builder
generated: 2026-04-02
format: markdown
---

SVG filters are a powerful tool that allows you to create unique text effects, images and other geometrical object effects. It lets you transform your plain objects in truly gorgeous, playful and interesting ways.

SVG Filter Builder Website

## Introduction

An SVG filter effect consists of a series of graphics operations that are applied to a given source vector graphic to produce a modified bitmapped result.

Filter effects are defined by the <filter> element and can be applied by referencing it in your SVG graphic elements using the filter property:

*-- CODE language-svg --  
<svg>  
   <filter id="myfilter">  
       ...  
   </filter>  
   <rect x="20" y="20" width="100" height="100" filter="url(#myfilter)"/>  
</svg>*

Creating complex filters is, however, a challenging task to do for users with little SVG filter effects experience. Users first need to study the different kinds of filter primitives and then study how they can be combined to create a filter that matches their needs.

## SVG Filter Builder to the Rescue

Since we at client IO are always excited about visual tools of all kinds, it was a natural move for us to build a visual designer that allows users to not only learn about SVG filters but also create them, share them with others and apply them in their diagrams.

> *Check out our Visual Filter Builder at* [*https://svgfilters.com*](https://svgfilters.com/)*.*

SVG Filter Builder

The first filter that you will see when you open the tool is the "Extruded" filter that displays a shadow effect on the default text. You can click on any of the filter primitives, e.g. the "Offset" primitive and try to change some of its properties. The preview is re-rendered as soon as you make any change. For example, you can try to move with the "dx" slider and see how the text shadow changes its offset:

Change filter properties and see live preview

You can also see the filter primitive SVG code in the bottom right corner of the Inspector panel. Clicking on the "Filter SVG" pane in the bottom bar shows you the SVG code of the entire combined filter:

Inspect the SVG filter source code

> TIP: Click on the "Get link" button in the same pane to get a link that you can send to anyone for them to see the exact same modified filter that you just created and be able to continue modifying it on their side.

The tool has some built-in graphic presets that you can test your filter on or you can add your own:

Inspect the SVG filter source code

You can add text, inline SVG or upload an image file in SVG/PNG/JPG formats.

The tool provides some built-in filters for you to try and experiment applying them to your graphics:

Try different built-in filters

... or you can create your own brand new filter either from a blank template, built-in template, inline SVG or by uploading an SVG file:

Try different built-in filters

Below you can find the list of filter primitives that you can experiment with:

Some of the filter primitives the tool supports

We hope you'll have a lot of fun playing with the SVG Filter Builder and also learn more about SVG filters in general.

We'd love to hear from you! Please use the community forum at <https://svgfilters.client.io/forum> or get in touch with the contact form at the bottom of the same page. We will also highly appreciate if you share the tool with others, e.g. using the "Tweet" button in the top right corner of the tool itself.

‍

Happy SVG Filtering!

*- The JointJS Team*