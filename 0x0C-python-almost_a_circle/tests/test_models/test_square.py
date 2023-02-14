import unittest
import io
import sys
import json
from pathlib import Path
from models.rectangle import Rectangle
from models.base import Base

class TestSquare(unittest.TestCase):
    def test_init(self):
        s = Square(10, 0, 0, 1)
        self.assertEqual(s.size, 10)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)
        self.assertEqual(s.id, 1)
        
    def test_str(self):
        s = Square(10, 0, 0, 1)
        self.assertEqual(str(s), '[Square] (1) 0/0 - 10')
        
    def test_width_height(self):
        s = Square(10, 0, 0, 1)
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)
        s.width = 20
        self.assertEqual(s.width, 20)
        self.assertEqual(s.height, 20)
        s.height = 30
        self.assertEqual(s.width, 30)
        self.assertEqual(s.height, 30)
        with self.assertRaises(TypeError):
            s.width = 'abc'
        with self.assertRaises(TypeError):
            s.height = 'abc'
            
    def test_update(self):
        s = Square(10, 0, 0, 1)
        s.update(1, 2, 3, 4)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)
        s.update(x=12, size=7, id=89)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 7)
        self.assertEqual(s.x, 12)
        self.assertEqual(s.y, 4)
        
    def test_to_dictionary(self):
        s = Square(10, 0, 0, 1)
        d = {'id': 1, 'size': 10, 'x': 0, 'y': 0}
        self.assertDictEqual(s.to_dictionary(), d)
        
if __name__ == '__main__':
    unittest.main()
