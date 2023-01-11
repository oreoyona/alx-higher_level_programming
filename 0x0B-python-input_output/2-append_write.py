#!/usr/bin/python3
"""Defines the append_write function."""

def append_write(filename="", text=""):
    """Appends a string to the end of a file
    Args:
        filename (str): The name
        text (str): The string.
    Returns:
        The number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
