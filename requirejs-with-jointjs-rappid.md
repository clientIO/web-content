---
source: https://www.jointjs.com/blog/requirejs-with-jointjs-rappid
generated: 2026-03-25
format: markdown
---

JointJS and JointJS+ now have full AMD/RequireJS support. In the past, a [shim](https://requirejs.org/docs/api.html) was needed to use JointJS or JointJS+ in a RequireJS project. That is no longer the case. All that is needed are these simple steps:

- Configure the paths to JointJS/JointJS+ and its dependencies
- Load JointJS/JointJS+ via require() or define() method
- *[optional]* Set JointJS/JointJS+ as a global dependency for all of your application's modules

## CONFIGURE THE PATHS TO JOINTJS/JOINTJS+ AND ITS DEPENDENCIES

In your application's HTML file, you will need to first load RequireJS. Then you will need to load two JavaScript files; one that contains your RequireJS configurations and another that contains code for initializing your application. Here is a sample **index.html** file:

-- CODE language-html --  
<script src="path/to/requirejs"></script>  
<script src="path/to/config.js"></script>  
<script src="path/to/main.js"></script>

And here is what your **config.js** would look:

-- CODE language-js --  
require.config({  
 paths: {  
 'rappid': 'path/to/jointjs/or/rappid',  
 // Dependencies for JointJS/Rappid:  
 'jquery': 'path/to/jquery',  
 'lodash': 'path/to/lodash',  
 'backbone': 'path/to/backbone'  
},  
 map: {  
 '\*': {  
 // Backbone requires underscore. This forces RequireJS to load lodash instead.             'underscore': 'lodash'  
 }  
 }  
});

## LOAD JOINTJS/JOINTJS+ VIA REQUIRE() OR DEFINE() METHOD

The starting point of your RequireJS application is usually a **main.js** or some similarly named file. Here's an example:

-- CODE language-js --  
// Load all your application's modules here.  
require(["path/to/some-module"], function () {  
  // Initialize application here.  
}, function (error) {  
  // Catches errors in case require fails.  
  console.log(error);  
});

And for a module that needs JointJS/JointJS+, you would require it as a dependency, like this:

-- CODE language-js --  
define(["joint"], function (joint) {  
  var graph = new joint.dia.Graph();  
  var paper = new joint.dia.Paper({  
    el: "<div/>".addClass("paper").appendTo("body"),  
    model: graph,  
  });  
‍  
  var rect = new joint.shapes.basic.Rect({  
    size: {  
      width: 40,  
      height: 40,  
    },  
    position: {  
      x: 160,  
      y: 160,  
    },  
  });  
  graph.addCell(rect);  
});

That's it! If you're using JointJS/JointJS+ in more than one module, you might want to consider setting it as a global dependency. See the next section for how to do that.

## JOINTJS/JOINTJS+ AS A GLOBAL DEPENDENCY

Setting JointJS/JointJS+ as a global dependency can be useful because then you won't have to load it explicitly for each individual module. Instead you will load it once in your main application file and then make it available to your application's global scope so that all of your application's modules have access to the joint namespace.

For example, here's how your **main.js** file would look with this setup:

-- CODE language-js --  
// Load global dependencies.  
require(["joint"], function (joint) {  
  // Set global dependencies here.  
  // These will be available to all AMD/RequireJS modules loaded after this point.  
  this.joint = joint;  
  
  // Now load all your application's modules here.  
  require(["path/to/some-module"], function () {  
    // Initialize application here.  
  }, function (error) {  
    // Catches errors in case require fails.  
    console.log(error);  
  });  
}, function (error) {  
  // Catches errors in case require fails.  
  console.log(error);  
});

And then one of your application's modules would look like this:

-- CODE language-js --  
define(  
  function () {  
    // Joint was already loaded and set as a global dependency.  
    // So we can use joint here without loading it again.  
    var graph = new joint.dia.Graph();  
    var paper = new joint.dia.Paper({  
      el: "<div/>".addClass("paper").appendTo("body"),  
      model: graph,  
    });  
    var rect = new joint.shapes.basic.Rect({  
      size: {  
        width: 40,  
        height: 40,  
      },  
      position: {  
        x: 160,  
        y: 160,  
      },  
    });  
    graph.addCell(rect);  
  },  
  function (error) {  
    // Catches errors in case require fails.  
    console.log(error);  
  }  
);

That's about it for using RequireJS with JointJS/JointJS+. As always, if you are experiencing troubles and need some help, you can reach us via several methods that can be found on our [support page](https://www.jointjs.com/support).