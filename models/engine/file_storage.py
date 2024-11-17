#!/usr/bin/python3
"""This module contains the FileStorage."""
import json


class FileStorage:
    """This Filestorage class allows for serializing and
    deserializing instances into a JSON file.
    """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary __objects where all instances
        are stored."""
        return self.__objects

    def new(self, obj):
        """Saves the object to the dictionary with a unique key."""
        if isinstance(obj, object) and isinstance(obj.id, str):
            self.__objects[f"{obj.__class__.__name__}.{obj.id}"]\
            = obj.to_dict()

    def save(self):
        """Serializes __objects to the json string and writes to __file_path."""
        if len(self.__file_path) != 0:
            with open(f"{self.__file_path}", "w", encoding="utf-8") as f:
                json.dump(self.__objects, f)

    def reload(self):
        """Deserializes the JSON file to __objects if JSON file exists."""
        try:
            with open(f"{self.__file_path}", "r", encoding="utf-8") as f:
                self.__objects = json.load(f)
        except (OSError, FileNotFoundError):
            pass
