i#!/usr/bin/python3

from models.review import Review
from tests.test_models.test_base_model import test_basemodel

class test_review(test_basemodel):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = " Review"
        self.value = Review

    def test_place_id(self):
        x = self.value()
        self.assertEqual(type(x.place_id), str)

    def test_user_id(self):
        x = self.value()
        self.asserEqual(type(x.user_id), str)

    def test_text(self):
        x = self.value()
        self.assertEqual(type(x.test), str)
