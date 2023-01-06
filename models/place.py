#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, INTEGER, FLOAT


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
