#!/usr/bin/env python3
"""
Module: task_01_pickle
Implements a custom class with pickle serialization/deserialization.
"""

import pickle


class CustomObject:
    """
    A simple class representing a custom object.
    """

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Prints the object's attributes in a readable format.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serializes the current instance to a file using pickle.

        Args:
            filename (str): The file where the object will be saved.
        """
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except (pickle.PickleError, OSError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserializes an object from a pickle file.

        Args:
            filename (str): The file to load the object from.

        Returns:
            CustomObject or None: The loaded object, or None if error occurs.
        """
        try:
            with open(filename, "rb") as file:
                obj = pickle.load(file)
                return obj if isinstance(obj, cls) else None
        except (FileNotFoundError, pickle.PickleError, EOFError, OSError):
            return None
