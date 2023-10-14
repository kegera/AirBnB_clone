#!/usr/bin/python3

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        jsondata = {}
        for key, value in self.__objects.items():
            jsondata[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as jsonfile:
            json.dump(jsondata, jsonfile)

    def reload(self):
        self.__objects = {}
        class_list = {
                'BaseModel': BaseModel,
                'User': User,
                'State': State,
                'City': City,
                'Amenity': Amenity,
                'Place': Place,
                'Review': Review
                }
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as jsonfile:
                jsondata = json.load(jsonfile)
                for key, value in jsondata.items():
                    class_name, obj_id = key.split(".")
                    self.__objects[key] = globals()[class_name](**value)
        except FileNotFoundError:
            pass


if __name__ == '__main__':
    storage = FileStorage()
    storage.reload()
