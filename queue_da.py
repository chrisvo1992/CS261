# Course: CS261 - Data Structures
# Student Name: Christopher Vo
# Assignment: Hw 2
# Description: Has class Queue that has methods to enqueue and dequeue values in
#a dynamic array
# Last revised: 10/12/2020

from dynamic_array import *


class QueueException(Exception):
    """
    Custom exception to be used by Queue class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class Queue:
    def __init__(self):
        """
        Init new queue based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.da = DynamicArray()

    def __str__(self):
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "QUEUE: " + str(self.da.length()) + " elements. ["
        out += ', '.join([str(self.da.get_at_index(_))
                          for _ in range(self.da.length())])
        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True is the queue is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.da.is_empty()

    def size(self) -> int:
        """
        Return number of elements currently in the queue
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.da.length()

    def enqueue(self, value: object) -> None:
        """
        This function takes a value as a parameter and will insert the value at the end of the array.
        Will raise QueueException if array is empty.
        """
        if self.size() == 0:
            self.da.append(value)
        else:
            self.da.insert_at_index(self.size(), value)

    def dequeue(self) -> object:
        """
        This function will remove the first value in array and return it.
        Will raise QueueException if array is empty.
        """
        if self.size() == 0:
            raise QueueException

        value = self.da.get_at_index(0)
        self.da.remove_at_index(0)

        return value


# BASIC TESTING
if __name__ == "__main__":

    print("\n# enqueue example 1")
    q = Queue()
    print(q)
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)

    print("\n# dequeue example 1")
    q = Queue()
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)
    for i in range(6):
        try:
            print(q.dequeue())
        except Exception as e:
            print("No elements in queue", type(e))