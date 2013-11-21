---
layout: default
title: "First Steps to Using Your Data"
author: aaron
category: "tutorial"
published: true
---

Using the instructions on the [download]({{ site.baseurl }}download/) page will get Harvest up and running super fast, which is awesome, but Harvest still won't be of much use because it won't be connected to your data. In this post I'll **outline** some of the steps you might follow to get Harvest connected to your data. This might not be enough information for everyone, so stay tuned for future posts, where I'll flesh out each of the steps and provide further hints on using Harvest day-to-day.

## Connect Harvest to Your Database

Database connections are handled by the Django framework and defined in the settings files at `myproject/conf`. Check out the [Django tutorial](https://docs.djangoproject.com/en/1.5/intro/tutorial01/#database-setup) on this topic for help, and look for detailed examples in a future post.

Once you connect to a new database (other than the SQLite database that comes with a new harvest project), you will have to rebuild the database tables used by Django and Harvest. Use `python bin/manage.py syncdb --migrate` in order to do this (don't worry, this command won't touch any existing tables in your database). Read about this command at the [Django docs](https://docs.djangoproject.com/en/1.5/ref/django-admin/#syncdb). (Pro hint: the `--migrate` option taps into functionality from [South](http://south.readthedocs.org/en/latest/commands.html#migrate)).

#### Homework

+ Django database setup: https://docs.djangoproject.com/en/1.5/intro/tutorial01/#database-setup
+ Django syncdb command: https://docs.djangoproject.com/en/1.5/ref/django-admin/#syncdb
+ South migrate command: http://south.readthedocs.org/en/latest/commands.html#migrate

## Model Your Data

Once your database is connected, you'll need to generate Django models for your data. If your data is already in the database, you can use `python bin/manage.py inspectdb`, which you can read about in the [Django docs](https://docs.djangoproject.com/en/1.5/ref/django-admin/#inspectdb).

If your data is not already in a relational database, you might choose to write Django models for your data manually and then write a Python script to extract your data from its current location, transform it as needed, and load it into the database you are using for Harvest (this process is called [ETL](http://en.wikipedia.org/wiki/Extract,_transform,_load)). Look for a future post with a detailed walk-through of this process. You can start by looking at the [Django model reference](https://docs.djangoproject.com/en/1.5/topics/db/models/).

After defining your models, you need to tell Harvest which model you want to use as the basis of your queries by defining `MODELTREES` in your `global_settings.py` file. Read about this setting in the [ModelTree docs](http://modeltree.harvest.io/ref/settings.html) and look for a future post about advanced ModelTree configuration.

#### Homework

+ Django inspectdb command: https://docs.djangoproject.com/en/1.5/ref/django-admin/#inspectdb
+ ETL definition: http://en.wikipedia.org/wiki/Extract,_transform,_load
+ Django model reference: https://docs.djangoproject.com/en/1.5/topics/db/models/
+ ModelTree settings: http://modeltree.harvest.io/ref/settings.html

## Create DataFields and DataConcepts

Now Harvest is connected to your data, but you need to define the way your data will appear in Harvest before you can start using it. A good place to start is with `python bin/manage.py avocado init myproject`, which will auto-generate Avocado DataFields for each of the fields in your Django models.

Then, you can create DataConcepts either at the command line or in the Django admin view (which you can view at the `http://localhost:8000/admin/` url if you are using the Django development server). Read about the admin view in the [Django tutorial](https://docs.djangoproject.com/en/1.5/intro/tutorial02/#enter-the-admin-site).

In order for a DataField to show up in the Harvest query view, it must be included in a DataConcept (that has a defined Formatter) and both the DataField and DataConcept must be published. A future post will cover this process in detail.

#### Homework

+ Django admin site: https://docs.djangoproject.com/en/1.5/intro/tutorial02/#enter-the-admin-site

## Contact Us for Help

For those of you who need more information (probably most people) to make your Harvest experience successful, stop in to the [chatroom]({{ site.baseurl }}chat/), join the listserv at https://groups.google.com/forum/#!forum/harveststack, or send us a direct email at info@harvest.io. We'd love to help.

---

