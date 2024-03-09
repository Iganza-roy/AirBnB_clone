#!/usr/bin/python3
"""Defines a class review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Customer review

    Attrs:
        place_id: Place id
        user_id: User id
        text: text
    """

    place_id = ""
    user_id = ""
    text = ""
