---
layout: default
title: "Download"
subtitle: "..and setup a new Harvest application."
---

All releases and release notes are posted on the repo's releases page on GitHub.

- [Harvest](https://github.com/chop-dbhi/harvest/releases/)
- [Avocado](https://github.com/chop-dbhi/avocado/releases/)
- [Serrano](https://github.com/chop-dbhi/serrano/releases/)
- [Cilantro](https://github.com/chop-dbhi/cilantro/releases/)

## Prerequisites

**Harvest requires Python 2.6 or 2.7 and Unix-based operating system (OS X, Linux, BSD).** Most systems come with Python pre-installed or can be easily installed uses the operating system's package manager. For general download and install instructions, visit [python.org's download page](http://python.org/download/).

To check if you have Python installed and the version:

```bash
which python && python --version
```

The output should look something like:

```bash
/usr/local/bin/python
Python 2.7.2
```

If you did not see anything, Python is not installed.

<div class="alert alert-block alert-info">
    <strong>Required stdlib modules.</strong> Harvest depends on the SSL and SQLite modules to be built in the standard library. If you are building Python from source, the OpenSSL and SQLite C headers must be installed prior to building Python. On CentOS, these are the sqlite-devel and openssl-devel packages.
</div>

## Pip - A Python Package Manager

In order to install the Harvest package (below), a Python package installer/manager must be installed. We recommend [Pip](http://www.pip-installer.org/en/latest/index.html) since it is the most prolific one available. To check if this is already installed, use the same command as above.

```bash
which pip
```

If nothing prints out, then do the following to fetch and install it. Note, you may have to add `sudo` after the pipe (`|`) if you are installing it globally on your system.

```bash
curl http://python-distribute.org/distribute_setup.py | `which python`
curl https://raw.github.com/pypa/pip/master/contrib/get-pip.py | `which python`
```

## Install the Harvest Package

The Harvest package is available on [PyPi](https://pypi.python.org/pypi/harvest) and can be installed using Pip. Again, you may need to prefix this with sudo if this is being installed globally on your system.

```bash
pip install harvest
```

## Create A New Harvest Project

Harvest comes with a command-line tool that sets up new projects with one command.

```bash
harvest init myproject
```

## Install The Harvest Demo

Not quite ready to dive in? The [Harvest demo]({{ site.baseurl }}demo/) can be installed with one line for you to play around with and inspect.

```bash
harvest init-demo openmrs
```

For full details on the available commands and options run `harvest --help` or for help with a specific command, run `harvest [command] --help`.

---

## Want Harvest a la Carte? 

As noted above, releases can be downloaded directly from GitHub or from the package's respective package managers.

Python-based components (Harvest, Avocado, and Serrano) are available on [PyPi](https://pypi.python.org/pypi).

- [Harvest](https://pypi.python.org/pypi/harvest) (command line tool)
- [Avocado](https://pypi.python.org/pypi/avocado)
- [Serrano](https://pypi.python.org/pypi/serrano)

Cilantro is the web client and only contains static files. For convenience, it can be installed using [Bower](http://bower.io) or the [Node Package Manager (NPM)](https://npmjs.org).

**Bower**

```bash
bower install cilantro
```

**NPM**

```bash
npm install cilantro
```
