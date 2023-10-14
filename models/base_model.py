#!/usr/bin/python3

import uuid
from datetime import datetime
import models


class BaseModel:
    """
    initialization of class BaseModel
    """
    def __init__(self, *args, **kwargs):
        """initialization"""
        if kwargs:
            for k, v in kwargs.items():
                if k == '__class__':
                    continue
                elif k == 'created_at' or k == 'updated_at':
                    setattr(self, k, datetime.fromisoformat(v))
                else:
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """return string representation of BaseModel"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
        updates public instance attribute updated_at
        with current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing key value pairs of __dict_"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
