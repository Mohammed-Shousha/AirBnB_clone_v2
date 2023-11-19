#!/usr/bin/python3
"""BaseModel class module"""

from uuid import uuid4
from datetime import datetime
from models import storage
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseModel():
    """
    BaseModel class
    Attributes:
        id (str): id of the instance
        created_at (datetime): time of creation
        updated_at (datetime): time of update
    Methods:
        __init__(self, *args, **kwargs)
        __str__(self)
        __save(self)
        to_dict(self)
    """

    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Initializes the instance"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue

                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")

                setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Returns the string representation of the instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the instance"""
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Returns the dictionary representation of the instance"""
        instance_dict = self.__dict__.copy()
        instance_dict["__class__"] = self.__class__.__name__
        instance_dict["created_at"] = self.created_at.isoformat()
        instance_dict["updated_at"] = self.updated_at.isoformat()
        return instance_dict

    def delete(self):
        """Delete the current instance from storage."""
        storage.delete(self)
