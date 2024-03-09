#!/usr/bin/python3
"""Defines a module place"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Location of BnB

    Attrs:
        city_id(str): City id
        user_id(str): User id
        name(str): Name of BnB
        description(str): Description of BnB
        number_rooms(int): number of rooms
        number_bathrooms(int): number of bathrooms
        max_guest(int): maximum number of guests
        price_by_night(int): Price by night
        latitude(float): latitude of place
        longitude(float): longitude of place
        amenity_ids(list): Amenity id
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
