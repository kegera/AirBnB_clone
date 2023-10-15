#!/usr/bin/python3

from models.user import User
from tests.test_models.test_base_model import test_basemodel

class test_User(test_basemodel):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        x = self.value()
        self.assertEqual(type(x.first_name), str)

    def test_last_name(self):
        x = self.value()
        self.assertEqual(type(x.last_name), str)

    def test_email(self):
        x = self.value()
        self.assertEqual(type(x.email), str)

    def test_password(self):
        x = self.value()
        self.assertEqual(type(x.password), str)
