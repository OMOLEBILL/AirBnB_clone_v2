#!/usr/bin/python3
"""This module uses Fabric to craete an archive"""


from datetime import datetime
from fabric.api import local, env, put, run
import os
env.hosts = ["54.164.163.118", "54.167.184.23"]
env.user = "ubuntu"


def do_pack():
    """We create a folder @version then store the archive """
    date_str = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = "web_static_{}.tgz".format(date_str)
    if not os.path.exists("versions"):
        local("mkdir -p versions")
    local("tar -cvzf versions/{} web_static".format(file_name))
    return "versions/{}".format(file_name) \
           if local("ls versions/{}".format(file_name)).succeeded else None

def do_deploy(archive_path):
    """ deploys the archive"""
    if not local("test -e {}".format(archive_path)).succeeded:
        return False
    file_name = archive_path.split("/")[-1]
    folder_name = file_name.split(".")[0]
    put(archive_path, "/tmp/")
    run("mkdir -p /data/web_static/releases/{}".format(folder_name))
    run("tar -xzf /tmp/{} -C /data/web_static/releases/{}".format(
        file_name, folder_name))
    run("rm /tmp/{}".format(file_name))
    run("rm -rf /data/web_static/current")
    run("ln -s /data/web_static/releases/{}/ /data/web_static/current".format(
        folder_name))
    return True
