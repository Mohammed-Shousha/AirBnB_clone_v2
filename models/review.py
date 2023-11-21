#!/usr/bin/python3
"""Review class module"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from os import getenv


class Review(BaseModel, Base):
    """
    Review class
    Attributes:
        place_id (str): the place id
        user_id (str): the user id
        text (str): the text of the review
    """
    if getenv("HBNB_TYPE_STORAGE", None) == 'db':
        __tablename__ = "reviews"
        place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        text = Column(String(1024), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""
