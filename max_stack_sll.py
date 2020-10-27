# Course: CS261 - Data Structures
# Student Name:
# Assignment:
# Description:


from sll import *


class StackException(Exception):
    """
    Custom exception to be used by MaxStack Class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MaxStack:
    def __init__(self):
        """
        Init new MaxStack based on Singly Linked Lists
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.sll_val = LinkedList()
        self.sll_max = LinkedList()

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "MAX STACK: " + str(self.sll_val.length()) + " elements. "
        out += str(self.sll_val)
        return out

    def is_empty(self) -> bool:
        """
        Return True is Maxstack is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.sll_val.is_empty()

    def size(self) -> int:
        """
        Return number of elements currently in the MaxStack
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.sll_val.length()

    # ------------------------------------------------------------------ #

    def push(self, value: object) -> None:
        """
        TODO: Write this implementation
        """
        self.sll_val.add_front(value)


    def pop(self) -> object:
        """
        TODO: Write this implementation
        """
        if self.sll_val.is_empty():
            raise StackException

        temp = self.sll_val.get_front()
        self.sll_val.remove_front()
        return temp

    def top(self) -> object:
        """
        TODO: Write this implementation
        """
        if self.sll_val.is_empty():
            raise StackException

        return self.sll_val.get_front()

    def get_max(self) -> object:
        """
        TODO: Write this implementation
        """
        if self.sll_val.is_empty():
            raise StackException

        return self.size()


# BASIC TESTING
if __name__ == "__main__":



    print('\n# get_max example 1')
    s = MaxStack()
    for value in [1, -20, 15, 21, 21, 40, 50]:
        print(s, ' ', end='')
        try:
            print(s.get_max())
        except Exception as e:
            print(type(e))
        s.push(value)
    while not s.is_empty():
        print(s.size(), end='')
        print(' Pop value:', s.pop(), ' get_max after: ', end='')
        try:
            print(s.get_max())
        except Exception as e:
            print(type(e))