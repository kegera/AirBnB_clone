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

    def test_create_storage(self):
        from models.engine.file_storage import FileStorage
        print(type(storage))
        self.assertEqual(type(models.storage), FileStorage)

    def test_dict(self):
        self.assertEqual(type(models.storage.all()), dict)

    def test_pathtype(self):
        self.assertEqual(type(models.storage._FileStorage__file_path), str)

    def test_reload(self):
        x = BaseModel()
        models.storage.save()
        models.storage.reload()
        for item in models.storage.all().values():
            ld = item
            self.assertEqual(x.to_dict()['id'], ld.to_dict()['id'])
