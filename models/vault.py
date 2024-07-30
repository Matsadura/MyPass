#!/usr/bin/python3
""" holds class Vault"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Vault(BaseModel, Base):
    """Representation of a vault """
    if models.storage_t == 'db':
        __tablename__ = 'vaults'
        user_id = Column(String(128), nullable=False)
        name = Column(String(128), nullable=False)
    else:
        user_id = ""
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes vault"""
        super().__init__(*args, **kwargs)
