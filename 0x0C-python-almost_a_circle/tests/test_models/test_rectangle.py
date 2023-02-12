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

    def test_area(self):
        r = Rectangle(2, 4, id=1)
        self.assertEqual(str(r), "[Rectangle] (1) 0/0 - 2/4")

    def test_display(self):
        self.assertEqual(self.rect1.display(),
                '\n\n  #####\n  #####\n  #####\n  #####\n  #####\n')
        self.assertEqual(self.rect2.display(), '\n ##\n ##\n ##\n')

    def test_str(self):
        self.assertEqual(str(self.rect1), '[Rectangle] (1) 2/3 - 10/5')
        self.assertEqual(str(self.rect2), '[Rectangle] (9) 1/0 - 2/3')

    def test_update_args(self):
        r = Rectangle(2, 4, id=1)
        r.update(3, 5, 7, 9, 11)
        self.assertEqual(r.id, 3)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 7)
        self.assertEqual(r.x, 9)
        self.assertEqual(r.y, 11)

    def test_update_kwargs(self):
        r = Rectangle(2, 4, id=1)
        r.update(width=5, height=7, x=9, y=11)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 7)
        self.assertEqual(r.x, 9)
        self.assertEqual(r.y, 11)

if __name__ == '__main__':
    unittest.main()
