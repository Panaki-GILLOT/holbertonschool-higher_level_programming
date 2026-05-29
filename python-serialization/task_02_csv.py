#!/usr/bin/env python3
"""
Module: task_02_csv
Converts CSV data into JSON format.
"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Converts a CSV file into a JSON file named data.json.

    Args:
        csv_filename (str): The CSV file to read.

    Returns:
        bool: True if successful, False otherwise.
    """
    try:
        data = []

        # Read CSV file using DictReader
        with open(csv_filename, mode="r", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data.append(row)

        # Write JSON output
        with open("data.json", mode="w", encoding="utf-8") as jsonfile:
            json.dump(data, jsonfile, indent=4)

        return True

    except FileNotFoundError:
        return False
    except (csv.Error, json.JSONDecodeError, OSError):
        return False
