import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.rect = Rectangle(5, 5, 0, 0, 1)
        
    def test_width_setter(self):
        self.rect.width = 10
        self.assertEqual(self.rect.width, 10)
        with self.assertRaises(TypeError) as cm:
            self.rect.width = '10'
        self.assertEqual(str(cm.exception), "width must be an integer")
        with self.assertRaises(ValueError) as cm:
            self.rect.width = 0
        self.assertEqual(str(cm.exception), "width must be > 0")
        
    def test_height_setter(self):
        self.rect.height = 10
        self.assertEqual(self.rect.height, 10)
        with self.assertRaises(TypeError) as cm:
            self.rect.height = '10'
        self.assertEqual(str(cm.exception), "height must be an integer")
        with self.assertRaises(ValueError) as cm:
            self.rect.height = 0
        self.assertEqual(str(cm.exception), "height must be > 0")
        
    def test_x_setter(self):
        self.rect.x = 10
        self.assertEqual(self.rect.x, 10)
        with self.assertRaises(TypeError) as cm:
            self.rect.x = '10'
        self.assertEqual(str(cm.exception), "x must be an integer")
        with self.assertRaises(ValueError) as cm:
            self.rect.x = -1
        self.assertEqual(str(cm.exception), "x must be >= 0")
        
    def test_y_setter(self):
        self.rect.y = 10
        self.assertEqual(self.rect.y, 10)
        with self.assertRaises(TypeError) as cm:
            self.rect.y = '10'
        self.assertEqual(str(cm.exception), "y must be an integer")
        with self.assertRaises(ValueError) as cm:
            self.rect.y = -1
        self.assertEqual(str(cm.exception), "y must be >= 0")
        
    def test_area(self):
        self.assertEqual(self.rect.area(), 25)
        
    def test_display(self):
        self.rect.display()
        
    def test_str(self):
        self.assertEqual(str(self.rect), "[Rectangle] (1) 0/0 - 5/5")
        
    def test_update(self):
        self.rect.update(5, 5, 5, 5, 5)
        self.assertEqual(str(self.rect), "[Rectangle] (5) 5/5 - 5/5")
        
if __name__ == '__main__':
    unittest.main()
