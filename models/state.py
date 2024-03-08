#!/usr/bin/python3
"""Defines a class State"""
from models.base_model import BaseModel


class State(BaseModel):
    """State where user is from

    Attributes:
        name (str): name of state
    """
    name = ""
