#!/usr/bin/python3
"""This module uses Fabric to craete an archive"""

from datetime import datetime
from fabric.api import local
import os


def do_pack():
    """We create a folder @version then store the archive """
    date_str = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = "web_static_{}.tgz".format(date_str)
    if not os.path.exists("versions"):
        local("mkdir -p versions")
    local("tar -cvzf versions/{} web_static".format(file_name))
    return "versions/{}".format(file_name) \
           if local("ls versions/{}".format(file_name)).succeeded else None
