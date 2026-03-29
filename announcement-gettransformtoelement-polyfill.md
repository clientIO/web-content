---
source: https://www.jointjs.com/blog/announcement-gettransformtoelement-polyfill
generated: 2026-03-29
format: markdown
---

Unfortunately, a new version of Chrome (48) [removes a feature](https://chromestatus.com/feature/5736166087196672) that is core to JointJS/JointJS+. This feature is the [SVGGraphicsElement.getTransformToElement()function](https://developer.mozilla.org/en-US/docs/Web/SVG). The motivation behind removing the method is - according to the Chrome team - open issues about [how this method is supposed to behave](https://lists.w3.org/Archives/Public/www-svg/2015Aug/att-0009/SVGWG-F2F-minutes-20150824.html#item02).

To overcome compatibility issues with future versions of Chrome, we prepared a polyfill that makes sure this method exists. Before a new version of JointJS/JointJS+ is released (or if you, for any reason, don't want to upgrade), include the following code before you load your application JavaScript:

**SVGElement.prototype.getTransformToElement = SVGElement.prototype.getTransformToElement ||        function(toElement) {**

**return toElement.getScreenCTM().inverse().multiply(this.getScreenCTM());**

**};**

Thanks!