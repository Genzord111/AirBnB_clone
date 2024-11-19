#!/usr/bin/python3
"""This module contains the BaseModel class """
from datetime import datetime
import uuid


class BaseModel:
    """This is the base class for managing
    user data and timestamps for creating and
    updating an instance"""
    def __init__(self, *args, **kwargs):
        """Initializes a new BaseModel with unique id and timestamps."""
        if kwargs != {}:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = kwargs['id']
                elif key == "created_at":
                    self.created_at =\
                            datetime.fromisoformat(kwargs['created_at'])
                elif key == "updated_at":
                    self.updated_at =\
                            datetime.fromisoformat(kwargs['updated_at'])
                elif key == "__class__":
                    pass
                else:
                    self.__setattr__(key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            from models import storage
            storage.new(self)

    def __setattr__(self, name, value):
        """Automatically updates 'updated_at' when attributes change."""
        super().__setattr__(name, value)
        if name != 'updated_at':
            self.__dict__["updated_at"] = datetime.now()

    def save(self):
        """Updates the updated_at timestamp"""
        self.updated_at = datetime.now()
        from models import storage
        storage.save()

    def to_dict(self):
        """Converts the instance to a dictionary with ISO format timestamps."""
        new_dict = {}
        new_dict['__class__'] = self.__class__.__name__
        for key, value in self.__dict__.items():
            if key == "updated_at" or key == "created_at":
                new_dict[key] = str(value.isoformat())
            else:
                new_dict[key] = value

        return new_dict

    def __str__(self):
        """Returns the string representation of the instance."""
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'
