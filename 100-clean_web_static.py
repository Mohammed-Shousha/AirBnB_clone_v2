#!/usr/bin/python3
# creates and distributes an archive to the web servers
from fabric.api import env, local, lcd, cd, run
import os

env.hosts = ["100.26.160.21", "52.90.13.8"]
env.user = "ubuntu"
env.key_filename = "my_private_key"


def do_clean(number=0):
    """Delete out-of-date archives."""

    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
