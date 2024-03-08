#!/usr/bin/python3
"""Defines a class City"""
from models.base_model import BaseModel


class City(BaseModel):
    """City in which BnB is located

    Args:
     state_id(str): State id
     name(str): city name
    """
    state_id = ""
    name = ""
