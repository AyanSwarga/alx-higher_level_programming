#!/usr/bin/python3
"""the module defines a function that adds attributes to objects"""

def add_attribute(obj, att, value):
    """add a new attribute to an object if possile"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
