#!/usr/bin/python3
"""
Contains the class DBStorage
"""

import models
from models.base_model import BaseModel, Base
from models.account import Account
from models.vault import Vault
from models.user import User
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

classes = { "Account": Account, "Vault": Vault, "User": User}


class DBStorage:
    """interaacts with the MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        MYPASS_MYSQL_USER = getenv('MYPASS_MYSQL_USER')
        MYPASS_MYSQL_PWD = getenv('MYPASS_MYSQL_PWD')
        MYPASS_MYSQL_HOST = getenv('MYPASS_MYSQL_HOST')
        MYPASS_MYSQL_DB = getenv('MYPASS_MYSQL_DB')
        MYPASS_ENV = getenv('MYPASS_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(MYPASS_MYSQL_USER,
                                             MYPASS_MYSQL_PWD,
                                             MYPASS_MYSQL_HOST,
                                             MYPASS_MYSQL_DB))
        if MYPASS_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()

    def get(self, cls, id):
        """Returns the object based on the class and its ID,
            or None if not found"""
        objs = self.all(cls).values()
        for obj in objs:
            if obj.id == id:
                return obj
        return None

    def count(self, cls=None):
        """
        Returns the number of objects in storage matching the given class.
        If no class is passed, returns the count of all objects in storage.
        """
        return len(self.all(cls).keys())
