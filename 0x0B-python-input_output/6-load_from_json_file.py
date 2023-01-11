#!/usr/bin/python3
"""Defines the load_from_json function."""
import json

def load_from_json_file(filename):
    """Loads an obj from a JSON file."""
    with open(filename) as f:
        return json.load(f)
