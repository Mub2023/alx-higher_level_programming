#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """class to test max integer function
    checks for expected Errors..
    and all posible right input."""

    def test_errors(self):
        """ Error test for max_integer most of errors
        """
        self.assertRaises(TypeError, max_integer, 22)
        self.assertRaises(TypeError, max_integer, True)
        self.assertRaises(TypeError, max_integer, {41, 10})
        self.assertRaises(TypeError, max_integer, ('m', 2), 'm')
        self.assertRaises(TypeError, max_integer, (5))
        self.assertRaises(TypeError, max_integer, ('x', 'c', 'd',
                                                   'c', 'f'), 'x')
        self.assertRaises(TypeError, max_integer, ('x', 11), 'x')
        self.assertRaises(TypeError, max_integer, (222))

    def test_working_int(self):
        """testing the 6-max_integer with int
        for any working int ."""
        self.assertEqual(max_integer([2000]), 2000)
        self.assertEqual(max_integer([3, 20]), 20)
        self.assertEqual(max_integer((21, 5)), 21)
        self.assertEqual(max_integer((-100, 20)), 20)
        self.assertEqual(max_integer([0, 55]), 55)
        self.assertEqual(max_integer([-22.5, 5.5]), 5.5)
        self.assertEqual(max_integer(()), None)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(''), None)
        self.assertEqual(max_integer(""), None)
        self.assertEqual(max_integer([-22, -5, False]), False)
        self.assertEqual(max_integer([[5, 5, 1], [99, 33], []]), [99, 33])
        self.assertEqual(max_integer([[55, 22], []]), [55, 22])
        self.assertEqual(max_integer([[], [], [11.5]]), [11.5])
        self.assertEqual(max_integer([[], [[55], [99.5]], [[11]], [[-21], [5]],
                                          [[-1.5], [5.5]]]), [[55], [99.5]])
        self.assertEqual(max_integer([{5, 5}, {6, 3, 1}, {25}]), {5, 5})
        self.assertEqual(max_integer([(30, 20, 10), (88, 99), ()]), (88, 99))

    def test_string(self):
        """testing it with string possible with ASCII chars"""
        self.assertEqual(max_integer(['z']), 'z')
        self.assertEqual(max_integer(['a', 'z']), 'z')
        self.assertEqual(max_integer('mub'), 'u')
        self.assertEqual(max_integer('m'), 'm')
        self.assertEqual(max_integer(['aaa', 'bbb', 'cx']), 'cx')


if __name__ == '__main__':
    unittest.main()
