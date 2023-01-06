#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, INTEGER, FLOAT, Table
from sqlalchemy.orm import relationship
import models
from os import environ

storage_engine = environ.get("HBNB_TYPE_STORAGE")

class Place(BaseModel, Base):
    """ A place to stay
    city_id =
    user_id
    name
    description
    number_rooms =
    number_bathrooms =
    max_guest =
    price_by_night =
    latitude =
    longitude =
    amenity_ids =
    """
    __tablename__ = "places"
    if (storage_engine == "db"):
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(INTEGER, default=0, nullable=False)
        number_bathrooms = Column(INTEGER, default=0, nullable=False)
        max_guest = Column(INTEGER, default=0, nullable=False)
        price_by_night = Column(INTEGER, default=0, nullable=False)
        latitude = Column(FLOAT, nullable=False)
        longitude = Column(FLOAT, nullable=False)
        amenity_ids = []
        reviews = relationship("Review", cascade = "all, delete", backref="place")
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []
        
        @property
        def amenities(self):
            """ getter function for amenity attribute """
            result = []
            tmp = models.dummy_classes['Review']
            for r in models.storage.all(tmp).values():
                if r.place_id == self.id:
                    result.append(r)
            return result