#!/usr/bin/python3
""" holds class Account"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Account(BaseModel, Base):
    """Representation of a account """
    if models.storage_t == 'db':
        __tablename__ = 'accounts'
        vault_id = Column(String(128), nullable=False)
        username = Column(String(128), nullable=True)
        email = Column(String(128), nullable=False)
        password_file = Column(String(128), nullable=False)
    else:
        vault_id = ""
        username = ""
        email = ""
        password_file = ""

    def __init__(self, *args, **kwargs):
        """initializes account"""
        super().__init__(*args, **kwargs)
