#!/usr/bin/python3
"""Defines the to_json_string function."""
import json

def to_json_string(my_obj):
    """Return the JSON version of my_obj."""
    return json.dumps(my_obj)
