from fabric.api import *

code_dir = "~/nbrubaker.com"

def checkout():
    with cd(code_dir):
        run("git pull")

def refresh():
    with cd(code_dir):
        run("jekyll")
        
def move_to_prod():
    with cd(code_dir + "_site"):
        run("sudo cp -r  * /var/www")
        
def deploy():
    checkout()
    refresh()
    move_to_prod()

