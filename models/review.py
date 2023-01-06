#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, String
import models
from sqlalchemy.orm import relationship


class Review(BaseModel, Base):
    """ Review class to store review information
    Arguments:
        Inherits from BaseModel and Base
        table name  = revies
        class attributes: text, place_id and user_id
    """
    __tablename__ = "reviews"
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    text = Column(String(1024), nullable=False)