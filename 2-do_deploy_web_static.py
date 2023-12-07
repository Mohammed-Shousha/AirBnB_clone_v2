#!/usr/bin/python3
# Fabfile to distribute an archive to a web server.
from os.path import exists
from fabric.api import env, put, run, local


env.hosts = ['100.26.160.21', '52.90.13.8']


def do_deploy(archive_path):
    """Deploys an archive to the web servers."""
    if not exists(archive_path):
        return False

    try:
        file = archive_path.split("/")[-1]
        name = file.replace('.tgz', '')

        path = "/data/web_static/releases/"

        put(archive_path, f"/tmp/{file}")

        run(f"mkdir -p {path}{name}/")
        run(f"tar -xzf /tmp/{file} -C {path}{name}/")

        run(f"rm /tmp/{file}")

        run(f"mv {path}{name}/web_static/* {path}{name}/")

        run(f"rm -rf {path}{name}/web_static")
        run("rm -rf /data/web_static/current")

        run(f"ln -s {path}{name}/ /data/web_static/current")

        return True
    except Exception:
        return False
