#!/usr/bin/python3
"""Defines a class review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Customer review"""
    place_id = ""
    user_id = ""
    text = ""
