---
source: https://www.jointjs.com/blog/svg-versus-canvas
generated: 2026-03-21
format: markdown
---

## Setting the scene

Choosing what technology to use can often be a time consuming process. A dilemma can often arise if you are unsure of the benefits or drawbacks of each prospective choice. This is understandable as the last thing you want is to choose a particular technology, and later realize you should have gone with a different option for one reason or another.

Debates about SVG versus Canvas are no different. A quick search on the topic will return a multitude of articles, and stackoverflow questions comparing the two technologies. It can be a daunting task to piece together all of the information in the hope of making a decision you can be confident in.  
  
In the following article, we will cover some of the same topics you have probably read about elsewhere, but hope to provide you with a more nuanced view. We will also shed some light on what implications those topics have for developers and business owners in practical terms.

Before getting into the weeds of the debate, in an article titled SVG versus Canvas, it would be remiss not to at least mention some of the basic differences between the two technologies at the outset, so let’s get to it!

## Vectors and Pixels

Two households, both alike in creating visual content for the web, but fundamentally different in their approach. SVG (Scalable Vector Graphics) is an XML based markup language used to describe 2D vector graphics. Canvas, on the other hand, allows users to draw on the HTML Canvas element via a JavaScript API.

*Canvas code example:*

-- CODE language-svg --  
<canvas id="canvas"></canvas>  
<script>  
const canvas = document.getElementById("canvas");  
const ctx = canvas.getContext("2d");  
  
ctx.fillStyle = "green";  
ctx.fillRect(10, 10, 150, 100);  
</script>*‍*

*SVG code example:*

-- CODE language-svg --  
<svg>  
  <rect width="150" height="100" fill="green" />  
</svg>

From the beginning, SVG was developed as an open standard by [W3C](https://www.w3.org/) (the World Wide Web Consortium), that means it was designed specifically to work well with other web standards. Generally, you can think of SVG as declarative drawing instructions that can be added alongside your HTML.

The history of Canvas is a little more muddled. Originally introduced by Apple, it was later standardized by [WHATWG](https://whatwg.org/) (the Web Hypertext Application Technology Working Group). As Canvas was originally created as a proprietary element by Apple, its adherence to web standards is questionable, and still lacking in important areas to this day.

The most pertinent difference is how each technology presents its content. Canvas is raster based, meaning it’s arrays of pixels arranged on a grid, while SVG is vector based, meaning it uses mathematical metadata when describing a graphic. The advantage of the latter is that when zooming or scaling, SVG will maintain its integrity, remaining crisp and clean on different-sized monitors and resolutions. Canvas content, including text, doesn’t preserve clarity when resized.

A second, and at first glance, seemingly less important difference is that each SVG element is present in the [DOM](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model) (Document Object Model), while Canvas is represented as a sole element. The reason why this is relevant will become more apparent later.

Now that we have established that both technologies can draw stuff, let’s dig a little deeper on some important aspects to consider when making decisions about SVG and Canvas.

## Accessibility: What happens in Canvas, stays in Canvas

A blazingly fast ™ website with incredible content is all for nothing if it’s not accessible to its users. The same idea can be applied to creating information-rich visual graphics, and the technology you choose to create those graphics can play an integral role in determining just how accessible they are.

If you want to talk about people with disabilities, they represent 16% of the global population according to the [World Health Organization](https://www.who.int/news-room/fact-sheets/detail/disability-and-health#:~:text=An%20estimated%201.3%20billion%20people%20%E2%80%93%20or%2016%25%20of%20the%20global,diseases%20and%20people%20living%20longer.). While all of those people obviously don’t use assistive software to navigate the web, the number is difficult to ignore if you are a business owner who wants to broaden their user base, or if you are worried about the [huge influx of lawsuits](https://www.shrm.org/resourcesandtools/hr-topics/behavioral-competencies/global-and-cultural-effectiveness/pages/record-number-of-lawsuits-filed-over-accessibility-for-people-with-disabilities.aspx) regarding the inaccessible web in recent years. Not only is accessibility a good business practice, but it’s the right thing to do in order to create the best experience for everybody.

In light of this, how do SVG and Canvas stack up against each other in terms of accessibility? Earlier, we mentioned that Canvas is a single element within the DOM. To put it frankly, this has huge repercussions for accessibility. Canvas doesn’t provide any information about the drawn content, nor does it expose any information to accessibility tools. [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/canvas#alternative_content_2) puts it rather bluntly:

***“In general, you should avoid using canvas in an accessible website or app.”***

In contrast, as SVG and all its content is in the DOM, it naturally conveys semantic meaning, and assistive technology can access sub-elements, text and links. As SVG was designed with web standards in mind, it can be further enhanced by accessibility standards such as [ARIA](https://www.w3.org/TR/wai-aria-1.2/#abstract) (Accessible Rich Internet Applications). That means what is visually represented in a graphic, can also be conveyed in the markup itself, allowing assistive software to get access to this information.

Is it possible to convey HTML Canvas content as markup? This is actually an important question in terms of Canvas and accessibility. The short answer is … it depends. Does your Canvas display some simple static shapes, or does it contain a complex interactive diagram? [W3C](https://www.w3.org/html/wg/spec/the-canvas-element.html) (The World Wide Web Consortium), the primary web standards organization, says the following:

***“When authors use the canvas element, they must also provide content that, when presented to the user, conveys essentially the same function or purpose as the canvas's bitmap. This content may be placed as content of the canvas element. The contents of the canvas element, if any, are the element's fallback content.”***

Fallback content in the form of a text description can certainly convey the characteristics of a simple static shape. When it comes to a dynamic diagram, providing fallback content that conveys the same function becomes a little more troublesome.

In fact, the [HTML specification](https://html.spec.whatwg.org/multipage/canvas.html#best-practices) says best practice is to include focusable elements as fallback content corresponding to each focusable part of the Canvas. At this point, you might be asking yourself, why not just use SVG in the first place?

Canvas is often sold as “not having to deal with the overhead of the DOM”. In terms of accessibility, that “overhead” is your users.

## Performance, a bird’s eye view

In a large proportion of articles and stackoverflow answers, performance is the main reason provided for choosing Canvas over SVG. The topic is often reduced to a one-liner such as “If you want to render 10,000 elements, use Canvas!”.  What more do you need to know, right?

An incorrect assertion that you may also come across in these discussions is that Canvas always outperforms SVG, but that’s not necessarily the case. SVG is actually more performant with a small number of objects, or over a large surface area. If you work with a small surface area, or a large number of objects, Canvas is out in front.

Other points that could be relevant are the type of content and the manner in which users will interact with your application, or if anything can be done to alleviate the performance advantage that Canvas has in some use cases.

Consider a scatter plot with 10,000 data points. Generally, this type of chart provides an overview of some dataset by plotting 2 variables, and suggests some correlation between them. The important information is gleaned from looking at the points as a whole, not at each one individually.

In terms of UI (User Interface),  you can assume the user doesn’t need to zoom in on each point, or that each circle would have child elements such as text or images. If you wanted to introduce a timeline to animate each point over time, you can certainly start reaching for Canvas as your tool of choice.

The type of information you need to visualize more often than not determines the manner in which it’s displayed. What if each data point needs to be an interactive card-like element with text, images, and action buttons? How will your users interact with this content?

Apart from it being less likely to have 10,000 data points you need to visualize in this manner, how important would it be to view all these elements as a whole? In this instance, the detail of each individual element is probably what users are most interested in, and the amount of these elements that could be viewed simultaneously in a useful way is certainly limited.

This begs the question, is there any strategy that could be employed to improve performance? On the remote chance that someone needed to view 10,000 information-rich elements as a whole, can a simple view of each element be rendered instead? After all, the element details wouldn’t be legible anyway. What about rendering only a subset of elements at a given time? In the age of “lazy loading”, a good use case would be to only render visible elements within the viewport, saving valuable milliseconds.

In fact some libraries, including JointJS, provide similar solutions already. JointJS can avoid rendering content which is not visible to the user. When deciding which technology to use, it may be worth your time asking similar questions. If the primary advantage of Canvas is somewhat diminished, are you willing to sacrifice all of the other benefits SVG provides?

## More meaningful testing with SVG

Ensuring your application behaves as expected is an integral part of the development process. In order to ascertain that your graphic functions correctly, debugging problems and testing functionality will be ingrained in your workflow.

Once again, when comparing Canvas and SVG, it’s difficult not to return to the fact that Canvas is a solitary HTML element in the DOM. This has numerous practical implications which may affect the speed or reliability of delivering your software.

Naturally, one of the first resources a developer will use when presented with a visual bug is to inspect an element in the DOM with developer tools. It’s a familiar process that can reveal a lot of crucial information quickly, such as if the element is even present in the DOM in the first place, or if it has the expected characteristics, and so on. This all contributes to identifying problems swiftly, and addressing them as needed.

As a lone Canvas element acts on the principle of what you see is what you get, developers are deprived of this point of contact with their applications, and will often have to pore over longer Canvas code to find an issue, losing valuable time in doing so.

In order to minimize the amount of debugging you have to do, you’ll probably want to introduce testing in your workflows. Since SVG and Canvas are both used to create graphics, it’s usually imperative that you test the UI (User Interface) of your applications. Some of the popular E2E (end-to-end) testing frameworks that are used to automate this process are [Cypress](https://www.cypress.io/), [Playwright](https://playwright.dev/), and [Selenium](https://www.selenium.dev).

One thing these frameworks have in common is that they work under the assumption that DOM elements are accessible. Elements are located via the concept of “Selectors”, a catch-all term that can include CSS selectors, accessibility roles, or even text. The fact that none of this information is readily available when using Canvas should immediately raise alarm bells.

If attempting to do E2E testing with Canvas, you’ll first likely have to write lots of custom code to locate the Canvas “elements”, then have to capture events on the Canvas element itself, or use some workaround to pretend to interact with elements without actually generating any DOM events.

The goal of E2E testing is to test applications from a real user’s perspective. Any makeshift solution that could be implemented with the aim of emulating this process for Canvas will simply never be a convincing substitute. The bottom line is, if you want to do authentic end-to-end testing of your UI, SVG is the way to go.

## What the heck is Foreign Object?

It might seem strange to focus on a specific SVG element as an advantageous reason for choosing SVG, but it’s not without merit. If a requirement for your graphic is to have interactive elements, developers are generally a habitual bunch. They will often reach for technologies they are familiar with, and in web land, the dominant force in this regard is still good old HTML.

‍[Foreign Object](https://developer.mozilla.org/en-US/docs/Web/SVG/Element/foreignObject) essentially allows the addition of HTML in your SVG elements. Embedding HTML text, creating basic interactive elements like buttons, or working with HTML inputs is all made a straightforward process. If you want to work with HTML on Canvas, a more unconventional approach such as rendering HTML on top of an underlying element will have to be adopted.

While this technique can be successful, it comes with a lot of additional complexity, such as the need to keep dimensions and position of the HTML in sync with the element itself. Taking advantage of foreign object in SVG allows you to create HTML-rich elements while avoiding some of the difficulties of other approaches.

Don’t believe us? Learn more about foreign object in SVG in our [JointJS tutorial](https://resources.jointjs.com/tutorial/foreign-object), and see what you can create.

## CSS and SVG play nicely

CSS is, and will remain one of the main pillars of the modern web. The ability to introduce uniform changes via CSS results in more maintainable applications. As SVG and CSS play nicely together, all of that CSS goodness extends to your SVG, allowing for even more modular code.

This integration is so seamless, it’s often overlooked just how easy it is to update some SVG styles using CSS pseudo-classes, such as [:hover](https://developer.mozilla.org/en-US/docs/Web/CSS/:hover). A painful amount of code has to be written in order to achieve similar functionality with Canvas.

Need to get creative with some more vibrant interactions? Animation is now ubiquitous online, and CSS allows the implementation of complex animations with relative ease, often outperforming any JavaScript equivalents. These animation techniques can be utilized with all DOM elements, including SVG.

CSS is not a static technology either. The evolution of CSS also means that your SVG code can evolve alongside it, benefiting from new standards and functionality, often adopted from CSS preprocessors. Component based architecture is ever present in the web world. With great new features like native CSS nesting, this architecture will be a mainstay for years to come, allowing for even more organization within SVG applications. As you can see, when evaluating a debate about Canvas versus SVG, those two technologies by themselves don’t paint the whole picture.

## Bits and Bobs

Not all facets of a debate about SVG and Canvas need to remain within the realm of the development world, there are also some external aspects which may be worth considering when choosing a technology, such as team structure, or how your content is viewed by search engines.

Teams usually consist of many roles, each member has their own strengths and type of work they focus on. Developers are often not the strongest designers, and as a result many teams will include both. The path to creating beautiful looking software, usually begins at the feet of designers. If you are lucky enough to have designers at your disposal, that means a lot of work can be entrusted to them, freeing up developers to focus on what they do best.

Need a beautiful set of icons for your startup idea? If working with SVG, this entire process can be taken care of by your design team without a lot of input from developers. Modern design tools like [Figma](https://www.figma.com/) or [Adobe illustrator](https://www.adobe.com/products/illustrator.html) allow the export of SVG, so an icon set can be passed to your development team upon completion, and embedded in your application with relative ease. As SVG is just markup, developers can update any other SVG properties as needed without any back and forth. As images for Canvas will always be static, extra coordination among team members is needed to ensure all image properties are in order before handing them over. Not to mention that you’ll need a little extra JavaScript to add the images to Canvas.

SEO (Search Engine Optimization) isn’t the first thing that pops into one’s mind when comparing Canvas and SVG, but it can certainly be beneficial to your business. SVG and Canvas both excel at complex graphics, but only one of them will be searchable and indexable.

At a basic level, when users are presented with a large amount of text, it’s possible even for most novices to utilize a *command/ctrl + F* command on their keyboard in order to find some relevant text. This simply isn’t possible with Canvas. A nice side effect of the DOM is that the text in SVG will also be indexable. Presenting crucial information in graphic form could be incredibly desirable depending on the use case. Using search engines like [Google](https://developers.google.com/search/blog/2010/08/google-now-indexes-svg), your users will be able to discover text content through your graphics when using SVG.

## Last thoughts on SVG

SVG and Canvas are both established technologies, so whichever one you choose, you will be supported by huge ecosystems and communities. Based on the points raised in this article, it won’t surprise you to find that our preferred tool of choice is SVG, but Canvas certainly has its use cases too.

In our opinion, the practical and ethical benefits of SVG far outweigh what Canvas has to offer, and if the performance benefit of Canvas can be mitigated with techniques such as virtual rendering, the question remains if you are willing to leave all of the advantages that SVG has to offer on the table? Lastly, if some milliseconds will make or break your application, it may be worth your time taking a look at the WebGL/WebGPU APIs instead of the Canvas API.