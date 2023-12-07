#!/usr/bin/python3
# Fabfile to distribute an archive to a web server.
from os.path import exists
from fabric.api import env, put, run, local, sudo


env.hosts = ['100.26.160.21', '52.90.13.8']
env.user = "ubuntu"
env.key_filename = "my_private_key"


def do_deploy(archive_path):
    """Deploys an archive to the web servers."""
    if not exists(archive_path):
        return False

    try:
        file = archive_path.split("/")[-1]
        name = file.replace('.tgz', '')

        path = "/data/web_static/releases/"

        put(archive_path, f"/tmp/{file}")

        sudo(f"mkdir -p {path}{name}/")
        sudo(f"tar -xzf /tmp/{file} -C {path}{name}/")

        sudo(f"rm /tmp/{file}")

        sudo(f"mv {path}{name}/web_static/* {path}{name}/")

        sudo(f"rm -rf {path}{name}/web_static")
        sudo("rm -rf /data/web_static/current")

        sudo(f"ln -s {path}{name}/ /data/web_static/current")

        print("New version deployed!")

        return True
    except:
        return False
