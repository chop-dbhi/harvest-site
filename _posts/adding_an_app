# Adding an app to your Harvest instance

Since Harvest is a set of Django apps, you can add any Django app to your project. As a beginner with databases, I wanted to add a tool that would allow me to import data into my Harvest project.

**Please note! I'm using the SQLite database that comes preattached to the Harvest project.**

## Where to install packages?
You need to install a package inside the virtual environment belonging to your Harvest project. That way the Harvest instance knows to load it.

## Virtual Environment Wrapper (virtualenvwrapper)
This is a handy tool that allows the user to easily find and manage virtual environments. [Installation instructions](http://virtualenvwrapper.readthedocs.org/en/latest/install.html)

Harvest works nicely with this tool: once you have installed and configured this tool, you can `init` a Harvest project with the `--venv-wrap` option and it will place the virtual environment where you've specified in your virtualenvwarpper configuration. That makes it really easy to find and control the environment.

## Where and how to install a Python package
If your package is on the Python Package Index (PyPI), then installation can be done through `pip`, the same command-line tool that you used to install Harvest. [Installation instructions](https://django-import-export.readthedocs.org/en/latest/installation.html)

Simply navigate to the directory where your virtual environments are located and activate (if the first time) or bring up (the virtualenvwrapper command is `workon projectname`. When the virtual environment is up, you can now install packages and they will go into that virtual environment.

## Adding your app to `INSTALLED_APPS`
Now, in your Harvest project's `global_settings.py` file, you'll need to add the name of your app to the list under `INSTALLED_APPS`. Then refer to the documentation of your particular package as to what else you need to create/modify in order to access the functionality of your specific package.

## What the import_export package does
Harvest is my first experience with database work. My current goal is to explore the tool itself, so for that purpose using the attached SQLite database is adequate. In order to populate this database with my own data, I needed a package that made this easier than writing my own python script.

There are several packages in the PyPi that offer this functionality. I choose this package because it had good documentation and supported the importaton of many different file types. (It also supports data export, but Harvest has that functionality included already). 

## After you install the import_export package
As this is an admin tool, you'll need to create (if you haven't already done so) an `admin.py` file among your project files.

The ResourceClass and AdminClass that you specify in this file allows the import_export tool how to work with your model.

```python
from django.contrib import admin
from projectname.models import Practice
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class PracticeResource(resources.ModelResource):

   class Meta:
      model = Practice #name of class
      import_id_fields = ['practice_id'] #you must specify your primary key if it is not the default 'id'.

class PracticeAdmin(ImportExportModelAdmin):

    resource_class = PracticeResource
    list_display = ('practice_id', 'care_model', 'risk_profile', 'size')

admin.site.register(Practice,PracticeAdmin)
```
This setup will allow you to import from a file (many formats supported) where the header rows match your model's field names. If they do not match exactly, you'll need to specify what those names are (otherwise the tool doesn't know what data goes where). Please refer to the documentation for [further information](https://django-import-export.readthedocs.org/en/latest/index.html) 

