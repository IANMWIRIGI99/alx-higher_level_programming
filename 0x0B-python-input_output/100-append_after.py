#!/usr/bin/python3
"""A function that inserts a line of text to a file, after
each line containing a specific string (see example)"""


def append_after(filename="", search_string="", new_string=""):
    """appends a line of new string after the line
    where the searched string is found"""
    with open(filename, 'r', encoding='UTF8') as f:
        tmp = f.readlines()

    with open(filename, 'w', encoding='UTF8') as f:
        for line in tmp:
            if search_string in line:
                line = line + new_string
            f.write(line)
