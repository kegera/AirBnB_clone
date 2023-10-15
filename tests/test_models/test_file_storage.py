#!/usr/bin/python3

import unittest
import os
import models
from models.base_models import BaseModel

class test_filestorage(unittest.Testcase):

    def test_new(self):
        x = BaseModel()
        for item in storage.all().values():
            y = x
            self.assertTrue(y is x)

    def test_all(self):
        x = BaseModel()
        y = models.storage.all()
        self.assertInstance(y, x)

    def test_empty(self):
        x = BaseModel()
        y = x.to_dict()
        x.save()
        z = BaseModel(**y)
        self.assertNotEqual(os.path.getsize('file.json'), 0)

    def test_save(self):
        x = BaseModel()
        models.storage.save()
        self.assertTrue(os.path.exists('file.json'))

    def envir(self):
        x_lst = []
        for k in models.storage._FileStorage__objects.keys():
            x_lst.append(k)
        for k in x_lst:
            del models.storage._FileStorage__objects[key]

    def rm_storage(self):
        try:
            os.remove('file.json')
        except Exception:
            pass
