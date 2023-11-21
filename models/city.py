#!/usr/bin/python3
"""City class module"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


class City(BaseModel, Base):
    """
    City class
    Attributes:
        state_id (str): the state id
        name (str): the name of the city
    """
    if getenv("HBNB_TYPE_STORAGE", None) == 'db':
        __tablename__ = "cities"
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey("states.id"), nullable=False)

        places = relationship("Place", backref="cities", cascade="delete")
    else:
        state_id = ""
        name = ""
