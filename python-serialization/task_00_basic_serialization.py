#!/usr/bin/env python3
"""
Basic serialization module
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary and save it to a JSON file.

    Args:
        data (dict): Data to serialize
        filename (str): Output JSON file name
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Load a JSON file and deserialize it into a Python dictionary.

    Args:
        filename (str): Input JSON file name

    Returns:
        dict: Deserialized Python dictionary
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
