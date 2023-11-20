#!/usr/bin/python3
"""DBStorage class module"""

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from os import getenv
from models.base_model import Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = {"Amenity": Amenity, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class DBStorage:
    """
    DBStorage class
    Attributes:
        __engine (sqlalchemy.Engine): The working SQLAlchemy engine
        __session (sqlalchemy.Session): The working SQLAlchemy session
    Methods:
        all(self, cls=None)
        new(self, obj)
        save(selfsession
        delete(self, obj=None)
        reload(self)
    """
    __engine = None
    __session = None

    def __init__(self) -> None:
        """Initialize a new DBStorage instance"""
        my_sql_user = getenv("HBNB_MYSQL_USER")
        my_sql_pwd = getenv("HBNB_MYSQL_PWD")
        my_sql_host = getenv("HBNB_MYSQL_HOST")
        my_sql_db = getenv("HBNB_MYSQL_DB")
        hbnb_env = getenv("HBNB_ENV")

        self.__engine = create_engine(
            f"mysql+mysqldb://{my_sql_user}:{my_sql_pwd}@{my_sql_host}/{my_sql_db}",
            pool_pre_ping=True
        )

        if hbnb_env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the curret database session all objects of the given class.

            If cls is None, queries all types of objects.
        """
        if cls is None:
            for clss in classes:
                objs = []
                objs.extend(self.__session.query(classes[clss]).all())
        else:
            if type(cls) is str:
                cls = eval(cls)
            objs = list(self.__session.query(cls).all())

        return {f"{type(obj).__name__}.{obj.id}": obj for obj in objs}

    def new(self, obj):
        """Add obj to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes to the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj from the current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database and initialize a new session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
