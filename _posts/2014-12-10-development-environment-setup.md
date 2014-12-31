---
layout: default
title: "Setting Up a Development Environment"
author: don
category: tutorial
published: true
date: 2014-12-10
---

This page provides instructions for setting up a local environment for developing and testing Avocado, Cilantro, and Serrano. To begin, checkout a local copy of the following repositories:

 * [Cilantro](https://github.com/chop-dbhi/cilantro)
 * [Avocado](https://github.com/chop-dbhi/avocado)
 * [Serrano](https://github.com/chop-dbhi/serrano)
 * [Harvest OpenMRS](https://github.com/chop-dbhi/harvest-openmrs)

Navigate to the OpenMRS directory and switch to the demo branch with:

```bash
git checkout demo
```

I suggest doing the following steps after setting up a [virtual environment](https://virtualenv.readthedocs.org/en/latest/) so all the modules installed with pip won't conflict with other projects. Whether you choose the virtualenv approach or not, the remaining instructions remain the same. Also, for the remainder of this page, I will assume you have a common directory containing all the repos checked out above. If not, you will need to change paths as needed below.

First, install all the requirements as you normally would for OpenMRS using:

```bash
cd harvest-openmrs
pip install -r requirements.txt
```

Staying in the `harvest-openmrs` directory, install the local versions of Avocado and Serrano using the following commands. We use the `-e` option to install in [editable mode](https://pip.pypa.io/en/latest/reference/pip_install.html#editable-installs) and the `--no-deps` flag to avoid installing the Avocado and Serrano requirements. Of course, if you wish to install them, you can remove the `--no-deps` from the commands below.

```bash
pip install -e ../avocado --no-deps
pip install -e ../serrano --no-deps
```

At this point, changes you make in your local Avocado or Serrano instance will automatically be picked up and reflected by the running OpenMRS instance. Next, we need to achieve a similar setup for Cilantro. This can be done from the `harvest-openmrs` directory using:

```bash
rm -rf openmrs/static/cilantro
ln -s ../cilantro/local/ openmrs/static/cilantro
```

Now, we have symlinked the OpenMRS cilantro directory to the local build of our Cilantro project. To get automatic updates, we need to execute the following from the `cilantro` directory. NOTE: You may need to run `npm install` first for the following command to work.

```bash
grunt work
```

So long as the grunt work task is running, it will detect changes to JS and SCSS files and perform a new local build of the changed files which will be automatically reflected in the running OpenMRS instance by way of the symlink created above.

Now, all that is left to do is to start the OpenMRS server and you should have a running instance of the OpenMRS demo ready for testing any one of Avocado, Cilantro, and Serrano. Start the server by running the following from the `harvest-openmrs` directory.

```bash
./bin/manage.py runserver
```

Remember, the way we have configured everything, all changes to your local Avocado, Cilantro, and Serrano local codebases will be reflected in the running OpenMRS demo. If you do not want change detection and reflection, then ignore the steps above for the codebases that should not be reflected in Avocado. For example, let's say I wanted Avocado and Serrano to be the stable releases from PyPi and just test Cilantro changes. I would ignore the `pip install ...` steps for Avocado and Serrano above which means only my local Cilantro changes will be reflected in the demo.
