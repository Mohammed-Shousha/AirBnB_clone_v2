#!/usr/bin/python3
"""City class module"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class City(BaseModel, Base):
    """
    City class
    Attributes:
        state_id (str): the state id
        name (str): the name of the city
    """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
