---
layout: default
title: "Configuring Cilantro Like a Pro"
author: byron
category: tutorial
published: true
date: 2014-02-16
---

This is an overview and mini-tutorial on how you can configure Cilantro, Harvest's default HTML5 client, to suit your project's needs. The client is the most challenging component to get right for any application. It is the layer between what you as the developer intend your application to do and what the user actually does with it. Harvest originally grew from a single project with general enough needs that creating a framework was the logical next step. Since then (2009), our team has built many applications using Harvest for various clinical research domains.

One thing that became very apparent was the need or desire to customize the behavior of certain components to better suit the domain of the project. The example I will be using for the post is [Varify](https://github.com/cbmi/varify/), our open source clinical DNA sequencing analysis and data warehouse application built on top of Harvest. The characteristics of the data and the workflow requirements of this application challenged Harvest both from a "scale" standpoint, but more noticeably the user interface. As a result, Varify has been the primary driver in the recent evolution of Harvest.

### Varify vs. "Vanilla" Harvest

Harvest was created with a *discovery* workflow in mind. A researcher thinks about a question, comes to the application, browses the various available data, views some results and iterates. After tailoring the query conditions and output columns, the user may export the data to perform follow-up tasks such as a statistical analysis.

Varify must be tailored with an analysis workflow for filtering, disambiguating, and classifying genomic variants. Users of Varify know exactly what filters to apply and what data they want to see in order to evaluate the results. In addition, Varify must provide custom analysis and *knowledge capture* components to meet the needs of the users and the requirements of the grant.

As mentioned above, Varify also serves as a data warehouse for genomic sequence data. This includes samples, variants, sample-specific variant results, public variant annotations, sample cohorts, allele frequencies, and gene, phenotype and literature indexes. This presents two challenges: there is a lot of data that needs to be represented clearly in the interface, and the scale of the data is beyond what Cilantro (and Harvest in general) has needed to handle in the past.

The following sections will use the "cookbook-style" format of stating the problem first, proposing a solution, and ending with a brief discussion.

As of version [2.2.3](https://github.com/cbmi/cilantro/releases/2.2.3/), Cilantro has the beginnings of a configuration-driven approach for customizing its behavior and representation. This decision was driven by the [culmination](https://github.com/cbmi/cilantro/issues/313) [of](https://github.com/cbmi/cilantro/issues/370) [these](https://github.com/cbmi/cilantro/issues/390) [tickets](https://github.com/cbmi/cilantro/issues/404).

The goal of a configuration-driven approach is to make the easy changes _really_ easy and the hard or custom much easier to integrate. Prior to the plethora of tickets above (and more), developers would have to shoe-horn their custom views after Cilantro loaded and their session started. This would result in post-processing overhead to the client, but also, more severely, no ability to prevent unneeded requests to the server.

---

### Set a new welcome message

The default [welcome message](http://harvest.research.chop.edu/demo/query/) on Harvest's query page is tailored towards a discovery workflow and an unknown audience or domain. Being a general purpose tool, this of course was intentional. However, in many cases, being too general makes the application feel impersonal and empty.

This simple need to change the welcome led to the [template store API](http://cilantro.harvest.io/ref/template-store.html). It maps a name to a template function that will be used to construct the HTML string that will be rendered by Cilantro when the corresponding view is rendered. Using the example above, we can now do this:

```javascript
require(['cilantro'], function(c) {
    c.templates.set('welcome', function() {
        return '<h1>Welcome</h1>';
    });

    require(['cilantro/main'], function() {

    });
});
```

Although this is not an exciting example, it shows the simplicity of the API. Let's expand this example and customize the default main.js script in the Harvest project template. The file is located in `static/scripts/javascript/src/main.js`. By default, it looks like the following:

```javascript
define(['cilantro/main', 'project/csrf'], function(c) {

});
```

First let's create our template in `static/scripts/javascript/src/templates/welcome.html` (you will need to create the `templates` directory) with the same markup.

```html
<h1>Hello there!</h1>
```

We can modify the `main.js` module to look like this:

```javascript
define(['cilantro', 'tpl!project/templates/welcome.html'], (c, welcomeTemplate) {
    c.templates.set('welcome', welcomeTemplate);

    require(['cilantro/main', 'project/csrf']);
});
```

What this does is load the `cilantro` library prior to loading the bootstrapping module `cilantro/main` which opens the default session and renders the interface. Using this approach, we can set configuration options and set custom templates (for a real world example look at [Varify's configuration](https://github.com/cbmi/varify/blob/9094abbe86fc2b6260720711baa66c6e124b7ab7/varify/static/js/src/main.js#L57-L95)).

As of version 2.2.7, the template module path can set on the templates store directly, rather than needing to include it as a dependency. The above can be further simplified to:

```javascript
define(['cilantro'], function(c) {
    c.templates.set('welcome', 'tpl!project/templates/welcome.html');

    require(['cilantro/main', 'project/csrf']);
});
```

An introduction and explanation of the template store can be read on its [documentation page](http://cilantro.harvest.io/ref/template-store.html).

The above approach is what will be used and assumed for the remainder of the post. That is, any configuration options or custom templates will be set in this module and prior to requiring `cilantro/main`.

### Turn on/off graphs and stats

One of the primary goals of Harvest is to get useful information about the data in front of users quickly and with as little effort as possible. An example of this is when a user clicks on a concept on the query page and immediately sees a summary of the containing data. From the OpenMRS demo, clicking on the "Hemoglobin" concept will result in this interface. As a user you immediately see a description, simple stats, and a frequency distribution chart.

![hemoglobin concept]({{ site.baseurl }}media/articles/hemoglobin.png)

This is the default behavior for _all_ numerical data (and dates and times) since it suits the majority of cases. An example where this behavior _doesn't_ make sense can be seen in Varify, specifically with genomic coordinate of a variant. Genomic coordinate is composed of the chromosome and the position on the chromosome that a variant exists. For the purposes of a clinical analysis workflow, seeing a distribution of variant positions is not useful nor is the breakdown of variants per chromosome. 

Although each of these components (stats, chart, values) are loaded independently and asynchronously in the interface, these requests can be quite taxing on the server and database. If they provide no value to the users, we should be able to turn them off. As of Cilantro 2.2.6, we now can with a single configuration option.

In the case of Varify, most of the charts and stats provide little value, so for this we decided to disable all the charts and stats. This is done by setting the `chart` and `stats` options to `false` for data fields of the applicable types.

```javascript
define(['cilantro'], function(c) {
    c.config.set('fields.defaults.form.stats', false);
    c.config.set('fields.types.number.form.chart', false);
    c.config.set('fields.types.date.form.chart', false);
    c.config.set('fields.types.time.form.chart', false);
    c.config.set('fields.types.datetime.form.chart', false);

    // remaining setup and bootstrapping..
});
```

The `config` object has a `set` method that takes either an object that will be merged into the default Cilantro configuration options or a dot-delimited string representing a path in the configuration hierarchy. The above settings will ensure the charts and stats are not displayed and thus prevent sending requests to the server needed by those components.

### Logical data types

The example above describes the need to customize how data fields are represented even when they are the same underlying type as other fields. Even though a field may be of type "number", doesn't mean the default interface makes sense or is optimal for interacting with the field's data. This is the primary argument for needing "logical types".

A logical type is an arbitrarily named type that does not inherit any properties from other types. There is no type hierarchy; meaning no sub-types, no type "interfaces", etc. It is merely an organizational technique for a field or fields to be distinguished from other fields.

#### Aside: Granularity of Field and Concept options

Cilantro has three levels of granularity for field and concept configuration options. The first level are the global set of options for all fields or concepts and has the lowest precedence. The second level are options specific to the logical type of a field. The third level are instance-specific (based on a field or concept id) options and have the highest precedence. The layout looks as follows:

```javascript
var cilantro = {
    fields: {
        defaults: { ... },

        types: {
            number: { ... },
            // other types...
        },

        instances: {
            10: { ... },
            // other instances...
        }
    }
};
```

When resolving the configuration options, options are merged top-down: defaults, type, instance. The resulting options will be used when (in this case) rendering the query interface for a field.

Continuing with logical types, the `types` level in the hierarchy above maps options to the logical type of a field. The default logical type for a field is simply its standard (simple) data type such as number, string, date, etc. New data types can be defined for a field by setting the instance level options `type` option.

```javascript
c.config.set('fields.instances.10.type', 'info_only');
```

This sets the logical type of the field with id `10` to `info_only`. By itself, this is not particularly useful since the `info_only` type has no custom options defined for it. But that can also be easily changed.

```javascript
c.config.set('fields.types.info_only.form', {
    info: true,
    stats: false,
    chart: false,
    controls: false
});
```

The above options disables the stats, chart and query controls for any field with the `info_only` logical type. This provides a flexible and fine-grained way to customize the behavior and display of fields and concepts.

### Conclusion

The configuration-driven approach in Cilantro has proven to be an approachable and flexible architecture for our current Harvest applications, even within the first week of its existence.

Although there are only a few (but highly demanded) configuration options available, more are on the horizon. If you have a configuration option that you would like added go to the [Configuration Option Wishlist](https://github.com/cbmi/cilantro/issues/313) ticket on GitHub and add a comment describing the option and how you would use it.
