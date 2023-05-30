#!/usr/bin/python3
"""Define Nodes classes for singly-linked list."""


class Node:
    """Iniilalize a node for the list."""

    def __init__(self, data, next_node=None):
        """Define the node

        Args:
        data: The data of new node.
        next_node: the next node of the list.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Gets and sets the data of the new node"""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Set the next node of the list."""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Define the SinglyLinkedList."""
    def __init__(self):
        """Initailze the  SinglyLinkedList."""
        self.__head = None

    def sorted_insert(self, value):
        """add new node to the SinglyLinkedList.

        Args:
        value: The new node  to be add.
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            temp = self.__head
            while (temp.next_node is not None and
                    temp.next_node.data < value):
                temp = temp.next_node
            new.next_node = temp.next_node
            temp.next_node = new

    def __str__(self):
        """Defines the print() of SinglyLinkedList."""
        vals = []
        temp = self.__head
        while temp is not None:
            vals.append(str(temp.data))
            temp = temp.next_node
        return ("\n".join(vals))
