# Course: CS261 - Data Structures
# Student Name: Christopher VO
# Assignment: hw 2
# Description: Has Stack class that has methods to add, remove, pop, top, push values
#of a dynamic array.
# Last revised: 10/12/2020

from dynamic_array import *


class StackException(Exception):
    """
    Custom exception to be used by Stack class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class Stack:
    def __init__(self):
        """
        Init new stack based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.da = DynamicArray()

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "STACK: " + str(self.da.length()) + " elements. ["
        out += ', '.join([str(self.da.get_at_index(_))
                          for _ in range(self.da.length())])
        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True is the stack is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.da.is_empty()

    def size(self) -> int:
        """
        Return number of elements currently in the stack
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.da.length()

    def push(self, value: object) -> None:
        """
        This function takes a value as a parameter and will add it to current array
        """
        self.da.append(value)

    def pop(self) -> object:
        """
        This function will return the last value of current array and remove it from current array.
        """
        if self.size() == 0:
            raise StackException

        value = self.da.get_at_index(self.size() - 1)
        self.da.remove_at_index(self.size() - 1)

        return value

    def top(self) -> object:
        """
        This function will return the value at the end of current array without removing it.
        """
        if self.size() == 0:
            raise StackException

        return self.da.get_at_index(self.size() - 1)




# BASIC TESTING
if __name__ == "__main__":

    print("\n# push example 1")
    s = Stack()
    print(s)
    for value in [1, 2, 3, 4, 5]:
        s.push(value)
    print(s)

    print("\n# pop example 1")
    s = Stack()
    try:
        print(s.pop())
    except Exception as e:
        print("Exception:", type(e))

    for value in [1, 2, 3, 4, 5]:
        s.push(value)

    for i in range(6):
        try:
            print(s.pop())
        except Exception as e:
            print("Exception:", type(e))

    print("\n# top example 1")
    s = Stack()
    try:
        s.top()
    except Exception as e:
        print("No elements in stack", type(e))
    s.push(10)
    s.push(20)
    print(s)
    print(s.top())
    print(s.top())
    print(s)
