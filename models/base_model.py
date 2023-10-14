#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    BaseModel class: define all common attribute/methods
    """
    def __init__(self, *args, **kwargs):
        """
        Initalize a Basemodel instance

        Args:
            id: (string) - assign with a uuid when an instance is created

            created_at: (datetime) - assign with the current datetime

            updated_at: (dayetime) - assign with the current datetime
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs != {}:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()

    def __str__(self):
        """
        return an informal string representation
        """
        return f"[{__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        updates the public instance attribute with the current time
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        return a dictionary containing all keys of __dict__ of the instance
        Return:
            dict: dictionary contains all attribute
        """
        self.__dict__["__class__"] = __class__.__name__
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
        return self.__dict__
