---
layout: default
title: "Custom Controls in Cilantro"
author: byron
category: tutorial
published: true
date: 2014-02-23
---

This is the next article in the [Configuring Cilantro Like a Pro]({% post_url 2014-02-16-configuring-cilantro-like-a-pro %}) series. To recap, a configuration system is being integrated into Cilantro to make it simple for application developers to customize components in Cilantro to suit their data or domain needs. The first article discussed setting configuration options, creating and setting custom templates, and what Cilantro calls "logical data types". This article gives an overview and example of creating a custom query control.

### What is a query control?

A query control is the interface for setting query conditions. The minimum data that make up a query condition are the `concept`, `field`, `operator` and `value`. The `concept` and `field` ids uniquely identify a query condition and are set by the control itself, so the end user only has to supply the operator and value. In the screenshot from the first article, the input boxes above the chart represent a <strong>query control</strong> for the field Hemoglobin.

![hemoglobin concept]({{ site.baseurl }}media/articles/hemoglobin.png)

Since hemoglobin is numerical data and has a continuous range, two input boxes are used to allow setting the lower and upper bound of the range. When set, these inputs make up the `value` of the query condition. The dropdown with a value of "between" defines the `operator` of the query condition.

As an example, if the lower bound was set to 10, the query condition may result in this:

```javascript
{
    concept: 10,
    field: 5,
    operator: 'between',
    value: [10, 6400]
}
```

### Built-in Controls

Most data types have a common way to be represented in a query interface. Shown above, continous numerical requires an operator and lower and upper bound inputs. Categorical data is typically represented as a set of choices that can be selected. A search box if generally most fitting for free-text data.

For this reason, Cilantro comes with a set of built-in controls for each major _logical_ data type. They currently include:

- `date` and `number` - range-based query controls (like in the screenshot above)
- `infograph` - list of bars for representing categorical data
- `search` - control for searching and browsing available free-text choices

Two simpler controls are included for categorical data, `singleSelectionList` and `multiSelectionList` which are standard select and multi-select form fields.

### Creating a custom control

Although the built-in controls have proven to be suitable for most cases, custom controls are sometimes required for expressing domain-specific assumptions. As mentioned in the previous article, a primary driver of recent Cilantro development is [Varify](https://github.com/cbmi/varify/), the open source clinical DNA sequencing analysis application built on Harvest. Varify defines quite a few custom controls to better facilitate the clinical analysis workflow as well as integration some domain-specific assumptions for making the query controls easier to use.

We will walk through creating a real-world control defined in Varify that enables querying variants by the [SIFT prediction score](http://sift.jcvi.org/). For context, a SIFT prediction score is a number between 0 and 1 where a score less than or equal to 0.5 denotes a variant has a damaging effect, while a score greater than 0.5 has a tolerated (benign) effect.

Although some geneticists may know these cutoffs, it is certainly not first-hand knowledge. Furthermore requiring the user to enter an explicit score does not make sense since all that matters is whether a score falls in one of the two _categories_. A more suitable control would be a dropdown that contains the choices "Damaging" or "Tolerated" that the end user can choose from.

Before implementing the specifics of the SIFT control, let's quickly go over the requirements of a control and how it fits in to the rest of Cilantro. All controls are views and must inherit from one of the following base control classes (each correspond to a Marionette view class):

- `ControlView`
- `ControlItemView`
- `ControlCollectionView`
- `ControlCompositeView`
- `ControlLayout`

In most cases the `ControlLayout` class should be used to provide the most flexibility for laying all the UI components in the control. All controls must be able to do two things, `get` the state of the UI and return a query condition and `set` the state of the UI given a query condition. The control classes all implement a `get` and `set` method that do nothing by default.

As mentioned above, the `field` and `concept` ids uniquely identify a query condition and are set by the control itself. This is because controls are contained within a `FieldForm` which is contained in a `ConceptForm`. This hierarchy corresponds to how fields are associated to concepts in the Harvest data model. Since this is case, a control really only needs to worry about the operator and value and thus only needs to implement the `getValue`, `setValue`, `getOperator` and `setOperator` methods (which are used internally by the `get` and `set` methods).

Given what we know about the SIFT prediction score, we can first create the template to represent the control. As mentioned there are two possible categories the prediction score rated at.

```html
<select>
    <option value="damaging">Damaging</option>
    <option value="tolerated">Tolerated</option>
</select>
```

The first thing to do is set the template, define the reused UI elements and any events that we need to handle.


```javascript
var SiftControl = c.ui.ControlLayout({
    template: 'sift-control',

    ui: {
        'select': 'select',
    },

    events: {
        'change select': 'change'
    }
});
```

As mentioned in [templates API](http://cilantro.harvest.io/ref/template-store.html), the template name corresponds to a compiled template registered in the template store. This can be done a number of ways, either set in the `cilantro` configuration object before Cilantro loads or programmatically before the session starts. See the [first article]({% post_url 2014-02-16-configuring-cilantro-like-a-pro %}) for a reminder on how to do this.

The `ui` property is a [Marionette feature](https://github.com/marionettejs/backbone.marionette/blob/master/docs/marionette.itemview.md#organizing-ui-elements) which is a map of identifiers to CSS selectors scoped within this control. That is, once the control is rendered, we can refer to the `select` DOM element (as defined in the template) using the `ui` property, e.g. `control.ui.select`. This will be used below.

The `events` property is a [Backbone feature](http://backbonejs.org/#View-delegateEvents) which is a map of event + selector to the function handler to be called when the event is triggered. In this case, every time the `change` event is triggered by the `select` element, we want to call the `change` method on the control view. The `change` method is already defined by the control classes so we do not need to define it here.

Now that we have our helper code defined, we can now focus on the relevant `get*` and `set*` methods. Since the operator is what toggles between the "damaging" vs. "tolerated" category, the value is actually fixed in this case. Therefore our `getValue` method looks like this and no `setValue` needs to be implemented:

```javascript
    ...

    getValue: function() {
        return 0.5;
    }
    ...
```

The next task is handle getting the operator from the state of the UI. This can be done using a simple `if/else` block. As a side note, `lte` means "less than or equal to" and `gt` means "greater than"


```javascript
    ...
    getOperator: function() {
        if (this.ui.select.val() === 'damaging') {
            return 'lte';
        } else {
            return 'gt';
        }
    }
    ...
```

The final method that needs to be implemented is the `setOperator` which takes operator and must update the UI to represent the state.


```javascript
    ...
    setOperator: function(operator) {
        if (operator === 'lte') {
            this.ui.select.val('damaging');
        } else if (operator == 'gt') {
            this.ui.select.val('tolerated');
        }
    }
    ...
```

The final control view looks like this:


```javascript
var SiftControl = c.ui.ControlLayout({
    template: 'sift-control',

    ui: {
        'select': 'select',
    },

    events: {
        'change select': 'change'
    },

    getValue: function() {
        return 0.5;
    },

    getOperator: function() {
        if (this.ui.select.val() === 'damaging') {
            return 'lte';
        } else {
            return 'gt';
        }
    },

    setOperator: function(operator) {
        if (operator === 'lte') {
            this.ui.select.val('damaging');
        } else if (operator == 'gt') {
            this.ui.select.val('tolerated');
        }
    }
});
```

### Integrating a custom control

The controls API provides a _store_ just like the templates API which makes it simple for registering custom controls.


```javascript
c.controls.set('sift', SiftControl);
```

To use it with the SIFT field, the instance configuration option can be set:

```javascript
c.config.set('fields.instances.64.forms.controls', ['sift']);
```

### Conclusion

A core goal of Harvest is to facilitate data discovery by using the data itself to drive the application. This requires that the interfaces for interacting with the data are suitable for the domain and the data itself. Having the ability to create custom controls and quickly integrate them in the application makes Harvest as a whole that much more powerful for rapidly developing domain-specific applications.

We believe that custom controls are going be one or the primary "selling points" when evaluating Harvest for future projects. As a result, we've decided to begin development of a repository (yet to be named) for storing custom controls for different use cases. This repository will be community-driven and pull requests can be submitted at any time for integrating a custom control. For the time being any ideas for query controls can be added to the [query control wishlist](https://github.com/cbmi/cilantro/issues/437).
