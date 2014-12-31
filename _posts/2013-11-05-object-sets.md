---
layout: default
title: "Object Sets"
intro: "Working with sets without knowing set theory."
category: announcement
date: 2013-11-05
author: "byron"
---

An [ongoing design goal]({{ site.baseurl }}manifesto/) of Harvest is to expose just enough functionality to enable data discovery, but no more. This is a fine line since this greatly benefits new users, but [power users](http://en.wikipedia.org/wiki/Power_user) may find this a limitation. One area where this line exists is exposing users to [set theory](http://en.wikipedia.org/wiki/Set_theory) and [boolean logic](http://en.wikipedia.org/wiki/Boolean_algebra) in general. It is difficult for many people to quickly understand `(A and (B or (C and D)))`. The nesting of conditions (with all those parentheses) causes the eyes to squint until you realize you need to start with the innermost condition and work your way outward.

Aside from exposing users to these details, it is incredibly difficult to make a decent user experience interacting with these low-level concepts. The interface can quickly become complex and interactions become complicated. As a result, it is common for query applications to succumb to the demand of power users and eventually embed a command prompt for writing raw queries to the application.

![cathode terminal]({{ site.baseurl }}media/articles/cathode.png)

### Discovery is Iterative

One inherent characteristic of data discovery is its iterative nature. The question being asked is constantly being refined and tweaked as data is being assessed and [new knowledge is being gained along the way](http://en.wikipedia.org/wiki/I_know_that_I_know_nothing). Coming back to our example above, we can apply this knowledge gain and collapse each expression as it is evaluated:

```
M = C and D     // first iteration
N = B or M      // second
P = A and N     // third

X = P = (A and (B or (C and D)))
```

`X = P` is much easier to read and understand than `X = (A and (B or (C and D)))`. The point here is that each iteration produces a new building block to be [composed](http://en.wikipedia.org/wiki/Composability) into the next iteration (refinement) of the question.

**So how is Harvest going to accomplish this?** Object sets.

Each iteration produces a result that can be represented as an _object set_. Regardless of how complicated the query was getting there, the object set is now a single object that needs to be added into subsequent queries. Furthermore, object sets are not simply references to the underlying query, but they contain direct references to the objects themselves. This ensures you always get back the original objects as you originally saw them. Objects can be added or removed from the set, which makes it possible to refine a set over time.

Integration of object sets is the big feature scheduled for [version 2.3](https://github.com/chop-dbhi/harvest/issues?milestone=1&state=open).
