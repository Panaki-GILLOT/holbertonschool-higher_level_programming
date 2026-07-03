#!/usr/bin/env python3
"""
Module: task_00_intro
Generates personalized invitation files from a template and attendee data.
"""


def generate_invitations(template, attendees):
    """
    Generate invitation files by filling a template with attendee data.

    Args:
        template (str): The invitation template with placeholders.
        attendees (list): A list of dictionaries with attendee data.

    Each output file is named output_X.txt, where X is the attendee's
    position in the list, starting from 1. Missing placeholder values
    are replaced with "N/A".
    """
    if not isinstance(template, str):
        print("Error: template must be a string.")
        return

    if not isinstance(attendees, list) or not all(
            isinstance(attendee, dict) for attendee in attendees):
        print("Error: attendees must be a list of dictionaries.")
        return

    if not template:
        print("Error: Template is empty, no output files generated.")
        return

    if not attendees:
        print("Error: No data provided, no output files generated.")
        return

    placeholders = ["name", "event_title", "event_date", "event_location"]

    for index, attendee in enumerate(attendees, start=1):
        content = template
        for placeholder in placeholders:
            value = attendee.get(placeholder)
            if value is None:
                value = "N/A"
            content = content.replace("{" + placeholder + "}", str(value))

        filename = f"output_{index}.txt"
        with open(filename, "w", encoding="utf-8") as output_file:
            output_file.write(content)

        print(f"Generated: {filename}")
