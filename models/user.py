#!/usr/bin/python3
"""class user that inherits from BaseModel"""
from .base_model import BaseModel


class User(BaseModel):
    """public class attribute"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
