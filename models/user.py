#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class User(BaseModel, Base):
    """
    This class defines a user by various attributes
    email: the email of user
    password: the password of the user
    first_name: the name of the user
    last_name: the last name of the user
    """
    __tablename__ = "user"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
