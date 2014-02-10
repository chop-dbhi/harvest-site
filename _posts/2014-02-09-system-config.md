---
layout: default
title: "Configuring Your System for Harvest"
author: aaron
category: "tutorial"
published: true
---

A bash script for setting up a python development ready, Harvest-friendly system environment on CentOS 6 boxes. Intended for folks without much sysadmin or python experience, without interest in dealing with puppet or another config tool, who just want to get moving.

Two caveats:

1. These steps represent one way of doing things, not the way. This guide intentionally eschews justification in deference to brevity.
2. These steps are intended for CentOS 6 (64 bit arch) because that's the OS in which I do development. With minor modification, they would probably work on Redhat. With major modification, but similar intent, they would probably work on most Linux distros. Again in deference to brevity, I didn't try for universality.

### Make a user for shared app development

```bash
sudo useradd -m devuser
sudo chmod g+rwxs /home/devuser
```

### Add your own user to the devuser group

```bash
sudo usermod -a -G devuser `id -un`
newgrp devuser
```

### Add supplementary yum repos

```bash
mkdir /home/devuser/downloads
cd /home/devuser/downloads
wget http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm
sudo rpm -Uvh ./epel-release-6-8.noarch.rpm
```

### Install system packages and then upgrade everything

This list includes packages for a production deployment. Some needs may be differ depending on your choice of database and web server.

```bash
sudo yum install httpd-devel openssl-devel ncurses-devel rpm-devel apr-util-devel apr-devel glibc-devel memcached readline-devel bzip2 bzip2-devel bzip2-libs libpng-devel openldap-devel freetype fontconfig freetype-devel lapack-devel blas-devel libgfortran gcc-gfortran gcc 'gcc-c++' postgresql-devel zlib-devel libcurl-devel expat-devel gettext-devel nginx sqlite-devel vim python-devel gmp-devel man
sudo yum groupinstall "Development tools"
sudo yum upgrade
```

### Create `/home/devuser/local` and configure PATH

I'll break caveat 1 here to say that I chose `/home/devuser/local` as the install prefix so that if a sysadmin was able to run the above portion, the rest of the script can be run without root privileges of any kind (unlike installing to `/opt` or `/usr/local`). It is also extremely unlikely to conflict with other users or applications on your system (as installing to `/usr/local` might).

```bash
mkdir /home/devuser/local
echo 'export PATH=/home/devuser/local/bin:${PATH}' >> ~/.bashrc
source ~/.bashrc
```

### Compile and install python 2.7

This script was tested and I have been developing in python 2.7.3, but later 2.7.x versions are available (2.7.6 is the latest). It's up to you if you want to find the latest 2.7.x and use that instead, it most likely won't make a difference.

```bash
cd /home/devuser/downloads
wget http://www.python.org/ftp/python/2.7.3/Python-2.7.3.tgz
tar -xzf Python-2.7.3.tgz
cd Python-2.7.3
/bin/bash configure --enable-shared --prefix=/home/devuser/local
make
make install
```

At this point, executing `which python` should return `/home/devuser/local/bin/python`. If it doesn't, try reloading your shell session.

### Install pip and important python packages

```bash
cd /home/devuser/downloads 
wget https://raw.github.com/pypa/pip/master/contrib/get-pip.py
python get-pip.py
pip install distribute virtualenv uwsgi supervisor
```

### Install node.js, npm, and important node packages

```bash
wget http://nodejs.org/dist/node-latest.tar.gz 
tar -xzf node-latest.tar.gz
cd node-v*
./configure --prefix=/home/devuser/local && make install
cd /home/devuser/downloads
# As of writing, wget fails on the npmjs.org cert, but only because it is registered to nodejs.org
wget --no-check-certificate https://npmjs.org/install.sh -O install-npm.sh
/bin/bash install-npm.sh
npm install -g grunt-cli coffee-script
```

### Create a home for your webapps

```bash
mkdir /home/devuser/webapps
```
Now, you're ready to [download Harvest]({{ site.baseurl }}download/).

### Contact us for help

If you need more help, or just want to chime in with your experience, check out all these ways to [get in touch]({{ site.baseurl }}contact/)!

---

