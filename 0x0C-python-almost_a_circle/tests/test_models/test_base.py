#!/usr/bin/python3
"""unittest for base module"""
from unittest import TestCase
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os


class TestBase_ID(TestCase):
    """Test cases for the Base class"""

    def set(self):
        """Set up method to reset the number of objects before each test"""
        Base._Base__nb_objects = 0

    def test_for_id_mixd(self):
        Base._Base__nb_objects = 0
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base(33).id, 33)
        self.assertEqual(Base(None).id, 2)
        self.assertEqual(Base().id, 3)
        self.assertEqual(Base(-88).id, -88)

    def test_for_id_postive(self):
        """test the id attribute of the Base class"""
        Base._Base__nb_objects = 0
        b1 = Base(10)
        self.assertEqual(b1.id, 10)
        b2 = Base(20)
        self.assertEqual(b2.id, 20)

    def test_for_id_none(self):
        Base._Base__nb_objects = 0
        b3 = Base(None)
        self.assertEqual(b3.id, 1)

    def test_for_id_empty(self):
        Base._Base__nb_objects = 0
        b5 = Base()
        self.assertEqual(b5.id, 1)

    def test_for_id_negative(self):
        Base._Base__nb_objects = 0
        b4 = Base(-20)
        self.assertEqual(b4.id, -20)


class Test_Base_to_json_string(TestCase):
    """Test cases for to_json_string method"""
    def Base_test_id(self):
        Base._Base__nb_objects = 0

    def test_to_json_string_basic_Square(self):
        sq = Square(2, 1, 4, 44)
        dc = [sq.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(dc)) == 39)

    def test_to_json_string_basic_Rectangle(self):
        re = Rectangle(4, 5, 6, 2, 44)
        dc = [re.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(dc)) == 53)

    def test_to_json_string_type(self):
        re = Rectangle(4, 5, 6, 2, 44)
        sq = Square(2, 1, 4, 44)
        self.assertEqual(str, type(Base.to_json_string([re.to_dictionary()])))
        self.assertEqual(str, type(Base.to_json_string([sq.to_dictionary()])))

    def test_to_json_string_mixed(self):
        re = Rectangle(4, 5, 6, 2, 44)
        sq = Square(2, 1, 4, 44)
        dc = [re.to_dictionary(), sq.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(dc)) == 92)

    def test_to_json_string_empty_list(self):
        self.assertEqual(Base.to_json_string([]), '[]')

    def test_to_json_string_None(self):
        self.assertEqual(Base.to_json_string(None), '[]')

    def test_to_json_string_too_many_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 55)

    def test_to_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 42)


class Test_Base_save_to_file(TestCase):
    """Test for save to file method"""
    def test_tear_down(self):
        Base._Base__nb_objects = 0
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass
        try:
            os.remove("Square.json")
        except FileNotFoundError:
            pass

    def test_save_to_file_rectangle(self):
        re = Rectangle(4, 5, 6, 2, 44)
        Rectangle.save_to_file([re])
        with open("Rectangle.json", 'r') as rea:
            self.assertTrue(len(rea.read()) == 53)

    def test_save_to_file_basic_square(self):
        sq = Square(2, 1, 2, 42)
        Square.save_to_file([sq])
        with open("Square.json", 'r') as rea:
            self.assertTrue(len(rea.read()) == 39)

    def test_save_to_file_multiple_rectangles(self):
        re1 = Rectangle(2, 4, 1, 2, 42)
        re2 = Rectangle(4, 2, 2, 1, 24)
        Rectangle.save_to_file([re1, re2])
        with open("Rectangle.json", 'r') as rea:
            self.assertTrue(len(rea.read()) == 106)

    def test_save_to_file_multiple_squares(self):
        sq1 = Square(2, 1, 2, 42)
        sq2 = Square(4, 2, 1, 24)
        Square.save_to_file([sq1, sq2])
        with open("Square.json", 'r') as rad:
            self.assertTrue(len(rad.read()) == 78)

    def test_save_to_file_overwrite(self):
        sq = Square(2, 1, 2, 42)
        Square.save_to_file([sq])
        sq = Square(42, 42, 42, 42)
        Square.save_to_file([sq])
        with open("Square.json", 'r') as we:
            self.assertTrue(len(we.read()) == 42)

    def test_save_to_file_None(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as we:
            self.assertEqual("[]", we.read())

    def test_save_to_file_empty(self):
        Square.save_to_file([])
        with open("Square.json", "r") as we:
            self.assertEqual("[]", we.read())

    def test_save_to_file_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_save_to_file_too_many_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file([], 10)


class Test_Base_from_json_string(TestCase):
    """Test cases for from_json_string method."""

    def test_from_json_string_type(self):
        list_input = [{'id': 90, 'width': 15, 'height': 9}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list, type(list_output))

    def test_from_json_string_basic_rectangle(self):
        list_input = [{'id': 90, 'width': 11, 'height': 5}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_basic_square(self):
        list_input = [{'id': 90, 'size': 5}]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_multiple_rectangles(self):
        list_input = [
            {'id': 90, 'width': 11, 'height': 5},
            {'id': 99, 'width': 3, 'height': 9}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_multiple_square(self):
        list_input = [
            {'id': 89, 'size': 4},
            {'id': 98, 'size': 8}
        ]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_multiple_None(self):
        self.assertEqual([], Base.from_json_string(None))

    def test_from_json_string_multiple_empty(self):
        self.assertEqual([], Base.from_json_string('[]'))

    def test_from_json_string_multiple_no_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_from_json_string_multiple_too_many_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string([], 52)


class Test_Base_create(TestCase):
    """Test cases for create static method."""

    def test_create_basic_rectangle(self):
        dt = {'width': 4, 'height': 6, 'x': 6, 'y': 2, 'id': 52}
        r = Rectangle.create(**dt)
        self.assertDictEqual(r.to_dictionary(), dt)

    def test_create_basic_square(self):
        dt = {'size': 4, 'x': 6, 'y': 2, 'id': 52}
        s = Square.create(**dt)
        self.assertDictEqual(s.to_dictionary(), dt)


class Test_Base_load_from_file(TestCase):
    """Test cases for load_from_file method."""

    def test_load_from_file_rectangles(self):
        r1 = Rectangle(2, 4, 1, 2, 42)
        r2 = Rectangle(4, 2, 2, 1, 24)
        Rectangle.save_to_file([r1, r2])
        lst = Rectangle.load_from_file()
        self.assertDictEqual(lst[0].to_dictionary(), r1.to_dictionary())
        self.assertEqual(type(lst[0]), Rectangle)
        self.assertDictEqual(lst[1].to_dictionary(), r2.to_dictionary())
        self.assertEqual(type(lst[1]), Rectangle)

    def test_load_from_file_squares(self):
        s1 = Square(2, 1, 2, 42)
        s2 = Square(4, 2, 1, 24)
        Square.save_to_file([s1, s2])
        lst = Square.load_from_file()
        self.assertDictEqual(lst[0].to_dictionary(), s1.to_dictionary())
        self.assertEqual(type(lst[0]), Square)
        self.assertDictEqual(lst[1].to_dictionary(), s2.to_dictionary())
        self.assertEqual(type(lst[0]), Square)

    def test_load_from_file_no_file(self):
        lst = Rectangle.load_from_file()
        self.assertEqual(lst, [])

    def test_load_from_file_too_many_args(self):
        with self.assertRaises(TypeError):
            Base.load_from_file(42)

    def tearDown(self):
        Base._Base__nb_objects = 0
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass
        try:
            os.remove("Square.json")
        except FileNotFoundError:
            pass


class Test_Base_save_to_file_csv(TestCase):
    """Test cases for save_to_file_csv method."""

    def test_save_to_file_csv_basic_rectangle(self):
        r = Rectangle(2, 4, 1, 2, 42)
        Rectangle.save_to_file_csv([r])
        with open("Rectangle.csv", 'r') as we:
            self.assertEqual(we.read(), '42,2,4,1,2\n')

    def test_save_to_file_csv_basic_square(self):
        s = Square(2, 1, 2, 42)
        Square.save_to_file_csv([s])
        with open("Square.csv", 'r') as we:
            self.assertEqual(we.read(), '42,2,1,2\n')

    def test_to_json_string_csv_multiple_rectangles(self):
        r1 = Rectangle(2, 4, 1, 2, 42)
        r2 = Rectangle(4, 2, 2, 1, 24)
        Rectangle.save_to_file_csv([r1, r2])
        with open("Rectangle.csv", 'r') as we:
            self.assertEqual(we.read(), '42,2,4,1,2\n24,4,2,2,1\n')

    def test_to_json_string_csv_multiple_squares(self):
        s1 = Square(2, 1, 2, 42)
        s2 = Square(4, 2, 1, 24)
        Square.save_to_file_csv([s1, s2])
        with open("Square.csv", 'r') as we:
            self.assertEqual(we.read(), '42,2,1,2\n24,4,2,1\n')

    def test_save_to_file_csv_overwrite(self):
        s = Square(2, 1, 2, 42)
        Square.save_to_file_csv([s])
        s = Square(42, 42, 42, 42)
        Square.save_to_file_csv([s])
        with open("Square.csv", 'r') as we:
            self.assertEqual(we.read(), '42,42,42,42\n')

    def test_save_to_file_csv_None(self):
        Square.save_to_file_csv(None)
        with open("Square.csv", "r") as we:
            self.assertEqual("[]", we.read())

    def test_save_to_file_csv_empty(self):
        Square.save_to_file_csv([])
        with open("Square.csv", "r") as we:
            self.assertEqual("[]", we.read())

    def test_save_to_file_csv_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv()

    def test_save_to_file_csv_too_many_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv([], 42)

    def tearDown(self):
        Base._Base__nb_objects = 0
        try:
            os.remove("Rectangle.csv")
        except FileNotFoundError:
            pass
        try:
            os.remove("Square.csv")
        except FileNotFoundError:
            pass


class Test_Base_load_from_file_csv(TestCase):
    """Test cases for load_from_file_csv method."""

    def test_load_from_file_csv_rectangles(self):
        r1 = Rectangle(2, 4, 1, 2, 42)
        r2 = Rectangle(4, 2, 2, 1, 24)
        Rectangle.save_to_file_csv([r1, r2])
        lst = Rectangle.load_from_file_csv()
        self.assertDictEqual(lst[0].to_dictionary(), r1.to_dictionary())
        self.assertEqual(type(lst[0]), Rectangle)
        self.assertDictEqual(lst[1].to_dictionary(), r2.to_dictionary())
        self.assertEqual(type(lst[1]), Rectangle)

    def test_load_from_file_csv_squares(self):
        s1 = Square(2, 1, 2, 42)
        s2 = Square(4, 2, 1, 24)
        Square.save_to_file_csv([s1, s2])
        lst = Square.load_from_file_csv()
        self.assertDictEqual(lst[0].to_dictionary(), s1.to_dictionary())
        self.assertEqual(type(lst[0]), Square)
        self.assertDictEqual(lst[1].to_dictionary(), s2.to_dictionary())
        self.assertEqual(type(lst[0]), Square)

    def test_load_from_file_csv_no_file(self):
        lst = Rectangle.load_from_file_csv()
        self.assertEqual(lst, [])

    def test_load_from_file_csv_too_many_args(self):
        with self.assertRaises(TypeError):
            Base.load_from_file_csv(42)

    def tearDown_test(self):
        Base._Base__nb_objects = 0
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass
        try:
            os.remove("Square.json")
        except FileNotFoundError:
            pass


if __name__ == '__main__':
    unittest.main()
