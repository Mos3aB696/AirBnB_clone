#!/usr/bin/python3
"""class city that inherit from BaseModel"""
from .base_model import BaseModel


class City(BaseModel):
    """public class attribute"""

    state_id = ""
    name = ""
