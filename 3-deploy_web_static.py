#!/usr/bin/python3
# Fabfile to distribute an archive to a web server.
from os.path import exists
from fabric.api import env, put, run, local, sudo
from datetime import datetime

env.hosts = ['100.26.160.21', '52.90.13.8']
env.user = "ubuntu"
env.key_filename = "my_private_key"


def do_pack():
    """Generates a .tgz archive"""
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    file_path = f"versions/web_static_{date}.tgz"

    local("mkdir -p versions")

    archive_command = f"tar -cvzf {file_path} web_static"
    if local(archive_command).failed:
        return None

    return file_path


def do_deploy(archive_path):
    """Deploys an archive to the web servers."""
    if not exists(archive_path):
        return False

    file = archive_path.split("/")[-1]
    name = file.split(".")[0]
    file_path = "/data/web_static/releases/{}".format(name)
    tmp = "/tmp/" + name

    try:
        put(archive_path, "/tmp/")
        run("mkdir -p {}/".format(file_path))
        run("tar -xzf {} -C {}/".format(tmp, file_name))
        run("rm {}".format(tmp))
        run("mv {}/web_static/* {}/".format(file_name, file_name))
        run("rm -rf {}/web_static".format(file_name))
        run("rm -rf /data/web_static/current")
        run("ln -s {}/ /data/web_static/current".format(file_name))
        return True
    except:
        return False


def deploy():
    """creates and distributes an archive to the web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
