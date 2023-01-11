#!/usr/bin/python3
"""Defines the from_json_string function."""
import json

def from_json_string(my_str):
    """Return the Python object from a JSON object."""
    return json.loads(my_str)
