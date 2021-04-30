from unittest import TestCase

from src import Amigo


class Test(TestCase):
    def test_aggregate(self):
        self.assertEqual(Amigo.aggregate("email1", "email2"), {"codi": 200})

    def test_search_exist(self):
        self.assertEqual(Amigo.search("email1", "email2"), {"codi": 200})

    def test_delete(self):
        self.assertEqual(Amigo.delete("email1", "email2"), {"codi": 200})

    def test_search_no_exist(self):
        self.assertEqual(Amigo.search("email1", "email2"), {"codi": 500})
