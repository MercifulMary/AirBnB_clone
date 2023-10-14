#!/usr/bin/python3
"""This module create a User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class for managing user object"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
