---
layout: default
title: "Leave Your Data Alone"
author: byron
category: tips
published: false
date: 2013-10-27
---

A common need when working with clinical databases is connecting to the database with read-only permissions. At first glance, this could seem problematic if attempting to build an application on top of this data and additional tables need to be created. Harvest supports communicating to multiple databases transparently by using [Django's database routers](https://docs.djangoproject.com/en/1.5/topics/db/multi-db/#automatic-database-routing).

What this means is that the application tables (including all the Harvest-related tables, users, sessions, etc.) can exist in a separate database from the actual data of interest. Since Harvest is a data-driven application that **does not impose any required structure on the data model** (aside from common normalization practices), the existing database can exist as is and the application database can be used on the side.

Since this is so common, Harvest projects created as of version 2.2.0 default to using this behavior. For simplicity, the `harvest` database defaults to being a SQLite database, but the database backend can easily be changed in the settings file.
