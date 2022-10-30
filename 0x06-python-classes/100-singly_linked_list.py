#!/usr/bin/python3

""" A class Node that defines a node of a singly linked list
"""


class Node:
    """ Node of a singly linked list """
    def __init__(self, data, next_node=None):
        """ Initialises a node of a singly linked list
        Args:
        data (int): data that the node contains.
        next_node (Node): Next node in the list
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """returns data in the node"""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """returns next node"""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """sets the data of the next_node"""
        if not (isinstance(value, Node) or value is None):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """defines a singly linked list"""
    def __init__(self):
        """initializes singly linked list"""
        self.__head = None

    def __repr__(self):
        tmp = self.__head
        values = ""
        while tmp:
            values += "{:d}".format(tmp.data)
            tmp = tmp.next_node
            if tmp:
                values += "\n"
        return values

    def sorted_insert(self, value):
        """inserts a new Node into the correct sorted position in the list
        (increasing order)

        Args:
        value (Node): new node to be inseted
        """
        new_node = Node(value)
        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                   tmp.next_node.data < value):
                tmp = tmp.next_node
            new_node.next_node = tmp.next_node
            tmp.next_node = new_node
