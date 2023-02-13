#!/usr/bin/python3
""" creating a base class """
import json
import csv


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        """ initialize this method """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON rep of the list dictionaries"""
        
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON string representation of list_objs to a file """

        filename = cls.__name__ + ".json"
        if list_objs is None:
            list_objs = []
        list_dictionaries = [obj.to_dictionary() for obj in list_objs]

        with open(filename, "w") as f:
            f.write(cls.to_json_string(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation json_string """
        
        if json_string is None or not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set """
        
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = None
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ returns list of instances"""

        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as f:
                json_string = f.read()
                return [cls.create(**obj) for obj in
                        cls.from_json_string(json_string)]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Serializes in CSV """
        
        filename = "{}.csv".format(cls.__name__)
        if list_objs is None:
            list_objs = []
        with open(filename, "w") as f:
            writer = csv.writer(f)
            if cls.__name__ == "Rectangle":
                for o in list_objs:
                    writer.writerow([o.id, o.width, o.height, o.x, o.y])
            else:
                for o in list_objs:
                    writer.writerow([o.id, o.size, o.x, o.y])
                    
    @classmethod
    def load_from_file_csv(cls):
        """ Deserializes in CSV """
        filename = "{}.csv".format(cls.__name__)
        try:
            with open(filename, "r") as f:
                reader = csv.reader(f)
                if cls.__name__ == "Rectangle":
                    lst = [cls(int(row[0]), int(row[1]), int(row[2]),
                        int(row[3]), int(row[4])) for row in reader]
                else:
                    lst = [cls(int(row[0]), int(row[1]), int(row[2]),
                        int(row[3])) for row in reader]
                return lst
            except FileNotFoundError:
                return []
