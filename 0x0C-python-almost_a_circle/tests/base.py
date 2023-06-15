#!/usr/bin/python3
"""unittest for base module"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases for the Base class"""

    def set(self):
        """Set up method to reset the number of objects before each test"""
        Base._Base__nb_objects = 0

    def test_for_id(self):
        """test the id attribute of the Base class"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base(20)
        self.assertEqual(b2.id, 20)
        b3 = Base(None)
        self.assertEqual(b3.id, 2)

if __name__ == '__main__':
    unittest.main()
