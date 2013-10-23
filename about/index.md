---
layout: default
title: "About"
---

## What is Harvest?

Harvest is an open source framework for the rapid development of purpose-built data discovery web applications. Through our experience developing many data-intensive biomedical applications, our team at The Children’s Hospital of Philadelphia (CHOP) has been researching ways to lower the barriers for researchers and clinicians to explore their data. The result of our efforts is an open source framework called Harvest.

Harvest is designed to elucidate complex data models and enable interactive visual exploration of large data sets. It is composed of three primary components: Avocado, a dynamic query engine built on top of Django’s object relational mapper (ORM), Serrano, a REST API which exposes endpoints for clients, and Cilantro, a web application written in JavaScript using HTML5 and CSS3 technologies to enable interactive query and display of data.

From the [Harvest Manuscript](http://jamia.bmj.com/content/early/2013/10/16/amiajnl-2013-001825.full):

> Biomedical researchers share a common challenge of making complex data understandable and accessible as they seek inherent relationships between attributes in disparate data types. Data discovery in this context is limited by a lack of query systems that efficiently show relationships between individual variables, but without the need to navigate underlying data models. We have addressed this need by developing Harvest, an open-source framework of modular components, and using it for the rapid development and deployment of custom data discovery software applications. Harvest incorporates visualizations of highly dimensional data in a web-based interface that promotes rapid exploration and export of any type of biomedical information, without exposing researchers to underlying data models. We evaluated Harvest with two cases: clinical data from pediatric cardiology and demonstration data from the OpenMRS project. Harvest's architecture and public open-source code offer a set of rapid application development tools to build data discovery applications for domain-specific biomedical data repositories. All resources, including the OpenMRS demonstration, can be found at http://harvest.research.chop.edu.

Want to learn more about the vision behind Harvest, [read the Manifesto]({{ site.baseurl }}manifesto/).

## Is This Vaporware?

**No.** Head over to the [media & press page]({{ site.baseurl }}media/) to see a listing our nationally funded projects (that we are able to disclose).

## We Are Here To Help

There are lots of details to think about when setting up your own project since the best way to represent your data to end users is very much dependent on the intricacies of the data.

While we'd love to include a standard recipe here, production deployment environments can vary quite a bit. The CBMi team has deployed and maintains multiple production instances and we're happy to help you set up your own instance of Harvest and pass on the lessons we've learned.

From Django models to Harvest Concepts, sparse data to complete CRFs, we're here to help you get the most out of your data and make something great happen. We are happy to help you directly and put you in touch with others using Harvest for similar data needs. Contact us at cbmisupport@email.chop.edu

If you do create a production instance of Harvest, we'd appreciate a quick mention. Include a link back to Harvest http://harvest.research.chop.edu or a mention of [our manuscript](http://jamia.bmj.com/content/early/2013/10/16/amiajnl-2013-001825.full).
