#!/usr/bin/env python3
"""
Module: task_03_xml
Provides serialization and deserialization of a dictionary using XML.
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a Python dictionary into an XML file.

    Args:
        dictionary (dict): Data to serialize.
        filename (str): Output XML file name.
    """
    try:
        root = ET.Element("data")

        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)

        tree = ET.ElementTree(root)
        tree.write(filename, encoding="utf-8", xml_declaration=False)

    except (ET.ParseError, OSError, TypeError):
        return None


def deserialize_from_xml(filename):
    """
    Deserializes an XML file into a Python dictionary.

    Args:
        filename (str): XML file to read.

    Returns:
        dict or None: Reconstructed dictionary or None on failure.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        result = {}
        for child in root:
            result[child.tag] = child.text

        return result

    except (ET.ParseError, FileNotFoundError, OSError):
        return None
