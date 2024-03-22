#!/usr/bin/python3

""" review mode """

from models.base_model import BaseModel


class Review(BaseModel):

    """ Review model """

    place_id = ""
    user_id = ""
    text = ""
