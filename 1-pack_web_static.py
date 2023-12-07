#!/usr/bin/python3
"""
Fabric script that generates a tgz archive
from contents of the web_static folder of AirBnB Clone Repo
"""

from datetime import datetime
from fabric.api import local


def do_pack():
    """Generates a .tgz archive from the contents of the 'web_static' directory."""
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    file_path = f"versions/web_static_{date}.tgz"

    local("mkdir -p versions")

    archive_command = f"tar -cvzf {file_path} web_static"
    if local(archive_command).failed:
        return None

    return file_path
