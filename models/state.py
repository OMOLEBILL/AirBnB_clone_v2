#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship 


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="delete")
    
    """ Give the file storage its meaning """
    if getenv(HBNB_TYPE_STORAGE) != "db":
        @property
        def cities(self):
            """ Get the list of all City objects """
            city_list = []
            for city in list(models.storage.all(City).values()):
                if city.state.id == self.id:
                    city_list.append(city)
            return city_list
