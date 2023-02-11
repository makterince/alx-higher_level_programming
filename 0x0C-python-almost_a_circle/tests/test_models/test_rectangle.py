import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_instance(self):
        r1 = Rectangle(10, 2)
        self.assertIsInstance(r1, Rectangle)

    def test_width_setter(self):
        r1 = Rectangle(10, 2)
        r1.width = 12
        self.assertEqual(r1.width, 12)

    def test_width_setter_type_error(self):
        r1 = Rectangle(10, 2)
        with self.assertRaises(TypeError):
            r1.width = "12"

    def test_width_setter_value_error(self):
        r1 = Rectangle(10, 2)
        with self.assertRaises(ValueError):
            r1.width = -12

    def test_height_setter(self):
        r1 = Rectangle(10, 2)
        r1.height = 8
        self.assertEqual(r1.height, 8)

    def test_height_setter_type_error(self):
        r1 = Rectangle(10, 2)
        with self.assertRaises(TypeError):
            r1.height = "8"

    def test_height_setter_value_error(self):
        r1 = Rectangle(10, 2)
        with self.assertRaises(ValueError):
            r1.height = -8

    def test_x_setter(self):
        r1 = Rectangle(10, 2)
        r1.x = 8
        self.assertEqual(r1.x, 8)

    def test_x_setter_type_error(self):
        r1 = Rectangle(10, 2)
        with self.assertRaises(TypeError):
            r1.x = "8"

    def test_x_setter_value_error(self):
        r1 = Rectangle(10, 2)
        with self.assertRaises(ValueError):
            r1.x = -8

    def test_y_setter(self):
        r1 = Rectangle(10, 2)
        r1.y = 8
        self.assertEqual(r1.y, 8)

    def test_y_setter_type_error(self):
        r1 = Rectangle(10, 2)
        with self.assertRaises(TypeError):
            r1.y = "8"

    def test_y_setter_value_error(self):
        r1 = Rectangle(10, 2)
        with self.assertRaises(ValueError):
            r1.y = -8

if __name__ == '__main__':
    unittest.main()
