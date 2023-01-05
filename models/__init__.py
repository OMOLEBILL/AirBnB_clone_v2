#!/usr/bin/python3
""" Initialtes a storage object

- if the environmental variable 'HBNB_TYPE_STORAGE is set to be 'db',
    instantiates a database storage engine(DBStorage.)
- Otherwise, instantiates a fule storage engine (FileStorage).
"""
from os import getenv

if getenv("HBNB_TYPE_STORAGE") == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()