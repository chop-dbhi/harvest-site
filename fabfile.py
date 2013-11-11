from fabric.api import *

env.hosts = ['harvest.research.chop.edu']

def deploy():
    with cd('/home/devuser/webapps/harvest-site-static'):
        run('git pull')
        run('git submodule update --init')
        run('jekyll build')
