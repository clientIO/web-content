---
source: https://www.jointjs.com/blog/jointjs-rappid-with-chrome-v57-bug-alert
generated: 2026-04-02
format: markdown
---

We have an important alert for our Google Chrome users, that on March 14th Chrome version 57 will be released and it's been discovered it contains a bug which can break certain aspects of JointJS/JointJS+.

Any Google Chrome version 57 users (+ higher dev versions) should be aware of this potential risk and take the necessary steps to implement the workaround below until we release an update to JointJS/JointJS+ which fixed the issue with Chrome. We plan to release this update by the end of March.

Affected functionality is SVG transformations (specifically the SVGTransformList API), and therefore rendering of some diagrams in JointJS and JointJS+.

> *To reiterate: a new version of JointJS+ with a fix for Chrome will be released by the end of March, and in the meantime we are providing a workaround.*

## Applying The Workaround

Add this code anywhere ***after*** the JointJS/JointJS+ library is included, and ***before*** your application loads. The code snippet overwrites two JointJS/JointJS+ internal functions that deal with SVG transformations.

V.matrixToTransformString = function(matrix) {

        matrix || (matrix = true);

         return 'matrix(' + [

              matrix.a || 1,

              matrix.b || 0,

              matrix.c || 0,

              matrix.d || 1,

              matrix.e || 0,

              matrix.f || 0

       ] + ')';

    };

V.prototype.transform = function(matrix, opt) {

         var node = this.node;

         if (V.isUndefined(matrix)) {

              return (node.parentNode)

                   ? this.getTransformToElement(node.parentNode)

                   : node.getScreenCTM();

         }

         if (opt && opt.absolute) {

              return this.attr('transform', V.matrixToTransformString(matrix));

         }

         var svgTransform = V.createSVGTransform(matrix);

         node.transform.baseVal.appendItem(svgTransform);

         return this;

};

> *We highly recommend our* [*Update Subscriptions*](https://www.jointjs.com/pricing) *and* [*Support Plans*](https://www.jointjs.com/support) *to ensure you always have access to the latest version of JointJS+ as well as dedicated support whenever you need it.*

## Additional information

The original threads and workaround can be found in our user groups at Github and Google:

- Github thread:<https://github.com/clientIO/joint/issues/535>‍
- Google Groups thread:<https://groups.google.com/forum/#!searchin/jointjs/canary%7Csort:relevance/jointjs/RsTRa2ICSYY/TPFNxQ8KBAAJ>

## In Closing

We regret any issues that this Google Chrome bug may cause JointJS/JointJS+ users, and we're doing everything possible to minimize the impact.

If you have any questions or need assistance, please don't hesitate to reach out to us!

‍

Happy diagramming!

*- The JointJS Team*