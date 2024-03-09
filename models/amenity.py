#!/usr/bin/python3
"""Defines a class Amenity"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity of BnB

    Args:
        name(str): name of amenity
    """
    name = ""
