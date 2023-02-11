import unittest
from models.base import Base

class TestBase(unittest.Testcase):
    def test_id_none(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_id_specified(self):
        b1 = Base(12)
        b2 = Base(34)
        self.assertEqual(b1.id, 12)
        self.assertEqual(b2.id, 34)
