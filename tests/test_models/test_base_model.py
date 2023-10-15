#!/usr/bin/python3

from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os


class test_base_model(unittest.Testcase):

    def __init__(self, *rgs, **kwargs):
        super().__init(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def test_default(self):
        x = self.value()
        self.assertEqual(type(x), self.value)

    def test_save(self):
        x = self.value()
        x.save()
        k = self.name + "." + x.id
        with open('file.json', 'r') as jfile:
            y = json.load(jfile)
            self.assertEqual(y[k], x.to_dict())

    def test_to_dict(self):
        x = self.value()
        y = x.to_dict()
        self. asserEqual(x.to_dict(), y)

    def test_str(self):
        x = self.value()
        self.assertEqual(str(x), '[{}] ({}) {}'format(self.name, x.ide, x.__dict__))

    def test_created_at(self):
        x = self.value()
        self.assertEqual(type(x.created_at), datetime.datetime)

    def test_id(self):
        x = self.value()
        self.assertEqual(type(x.id), str)

    def test_updated_at(self):
        x = self.value()
        self.assertEqual(type(x.updated_at), datetime.datetime)
        y = x.to_dict()
        x = BaseModel(**y)
        self.assertFalse(x.created_at == x.updated_at)

    def setUp(self):
        pass

    def tearDown(self):
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_kwargs(self):
        x = self.value()
        y = x.to_dict()
        z = BaseModel(**y)
        self.assertFalse(z is x)

if __name__ == '__main__':
    unittest.main()
