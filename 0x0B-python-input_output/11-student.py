#!/usr/bin/python3
"""A class Student that defines a student"""


class Student:
    """Module of a student


    Attributes:
        first_name (str): Describes the 1st name of a student
        last_name (str): Describes the last name of a student
        age (int): Describes the age of a student
    """
    def __init__(self, first_name, last_name, age):
        """Initializes the student attributes


        Args:
            first_name (str): Describes the 1st name of a student
            last_name (str): Describes the last name of a student
            age (int): Describes the age of a student


        Returns:
            None
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        if attrs is None:
            return(self.__dict__)
        new_dict = {}
        for elm in attrs:
            if hasattr(self, elm):
                new_dict[elm] = getattr(self, elm)
        return(new_dict)

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        for elm in json:
            self.__dict__[elm] = json[elm]
