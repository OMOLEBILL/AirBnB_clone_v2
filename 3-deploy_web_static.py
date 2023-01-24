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
    if os.path.exists(archive_path):
        archived_file = archive_path[9:]
        newest_version = "/data/web_static/releases/" + archived_file[:-4]
        archived_file = "/tmp/" + archived_file
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(newest_version))
        run("sudo tar -xzf {} -C {}/".format(archived_file,
                                             newest_version))
        run("sudo rm {}".format(archived_file))
        run("sudo mv {}/web_static/* {}".format(newest_version,
                                                newest_version))
        run("sudo rm -rf {}/web_static".format(newest_version))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(newest_version))

        print("New version deployed!")
        return True

    return False


def deploy():
    """
    Deploy function do_pack and do_deploy.
    """
    path = do_pack()
    if path:
        return do_deploy(path)
    return False
