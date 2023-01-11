#!/usr/bin/python3
"""Defines the save_to_json function."""
import json


def save_to_json_file(my_obj, filename):
    """Save a file to JSON representation."""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
