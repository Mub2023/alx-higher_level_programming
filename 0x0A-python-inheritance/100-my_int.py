#!/usr/bin/python3
"""a class MyInt that inherits from int:
     is a rebel  has == and != operators inverted
"""


class MyInt(int):
    """this class is rebel age
    has == and != operators inverted
    """
    def __eq__(self, integer):
        """ changes the == to != """
        return self.real != integer

    def __ne__(self, integer):
        """ changes the != to == """
        return self.real == integer
