import unittest
import os
import csv
import json

class TestBase(unittest.TestCase):
    def setUp(self):
        self.test_data = [
                {"id": 1, "width": 1, "height": 1, "x": 0, "y": 0},
                {"id": 2, "width": 2, "height": 2, "x": 1, "y": 1}
        ]
        self.test_csv = "1,1,1,0,0\n2,2,2,1,1\n"
        
    def tearDown(self):
        try:
            os.remove("Rectangle.json")
        except:
            pass

        try:
            os.remove("Rectangle.csv")
        except:
            pass
        
    def test_to_json_string(self):
        self.assertEqual(Base.to_json_string(self.test_data),
                json.dumps(self.test_data))
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        
    def test_from_json_string(self):
        self.assertEqual(Base.from_json_string(json.dumps(self.test_data)),
                self.test_data)
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])
        
    def test_save_to_file(self):
        Base.save_to_file([Base.create(**data) for data in self.test_data])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), Base.to_json_string(self.test_data))

    def test_load_from_file(self):
        with open("Rectangle.json", "w") as f:
            f.write(Base.to_json_string(self.test_data))
            
        objs = Base.load_from_file()
        self.assertEqual(len(objs), 2)
        self.assertEqual(objs[0].to_dictionary(), self.test_data[0])
        self.assertEqual(objs[1].to_dictionary(), self.test_data[1])
        
    def test_save_to_file_csv(self):
        Base.save_to_file_csv([Base.create(**data) for data in self.test_data])
        with open("Rectangle.csv", "r") as f:
            self.assertEqual(f.read(), self.test_csv)
            
    def test_load_from_file_csv(self):
        with open("Rectangle.csv", "w") as f:
            f.write(self.test_csv)

        objs = Base.load_from_file_csv()
        self.assertEqual(len(objs), 2)
        self.assertEqual(objs[0].to_dictionary(), self.test_data[0])
        self.assertEqual(objs[1].to_dictionary(), self.test_data[1])
if __name__ == '__main__':
    unittest.main()
