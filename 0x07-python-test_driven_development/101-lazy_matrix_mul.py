#!/usr/bin/python3
"""
multiplies 2 matrices by using the module NumPy
Test cases should be the same as
100-matrix_mul but with new exception type/message
"""
import numpy as n


def lazy_matrix_mul(m_a, m_b):
    """Return the new matrix using numpy
    Arg: m_a: matrix 1
    m_b: matrix 2."""

    return (n.matmul(m_a, m_b))
