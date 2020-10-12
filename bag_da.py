# Course: CS261 - Data Structures
# Student Name: Christopher Vo
# Assignment: HW 2
# Description: Has Bag class that has methods to add, remove, count, or clear
#dynamic array elements
# Last revised: 10/12/2020

from dynamic_array import *


class Bag:
    def __init__(self, start_bag=None):
        """
        Init new bag based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.da = DynamicArray()

        # populate bag with initial values (if provided)
        # before using this feature, implement add() method
        if start_bag is not None:
            for value in start_bag:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "BAG: " + str(self.da.length()) + " elements. ["
        out += ', '.join([str(self.da.get_at_index(_))
                          for _ in range(self.da.length())])
        return out + ']'

    def size(self) -> int:
        """
        Return total number of items currently in the bag
        DO NOT CHANGE THIS CLASS IN ANY WAY
        """
        return self.da.length()


    def add(self, value: object) -> None:
        """
        This function will add a value to the current array.
        """
        self.da.append(value)

    def remove(self, value: object) -> bool:
        """
        This function will look through array and remove the value specified in the parameter.
        If value does not exist in array will return False. If value was found return True.
        """
        for i in range(self.size()):
            if self.da.get_at_index(i) == value: #will return True the first time specified value appears
                self.da.remove_at_index(i)
                return True
        return False

    def count(self, value: object) -> int:
        """
        This function will take a value as a parameter and will count how many times
        the value appears in the current array.
        """
        results = 0
        for i in range(self.size()): #Will count how many times value appears in array
            if value == self.da.get_at_index(i):
                results += 1

        return results

    def clear(self) -> None:
        """
        This function will remove all values in array.
        """
        for i in range(self.size()):
            self.da.remove_at_index(0)

    def equal(self, second_bag: object) -> bool:
        """
        This function will take a another bag as a parameter and will check if
        they share the same values and same length. Will return False if they are
        different sizes or if values are not shared between both bag objects.
        """

        if self.size() != second_bag.size(): #if sizes of bags are different
            return False

        for i in range(self.size()):#will take first value in bag and compare to every element in 2nd bag
            found = False
            for j in range(self.size()):
                if self.da.get_at_index(i) == second_bag.da.get_at_index(j):
                    found = True
            if found is False: #if 1 value is not found in the other bag then return False
                return False

        return True



# BASIC TESTING
if __name__ == "__main__":

    print("\n# add example 1")
    bag = Bag()
    print(bag)
    values = [10, 20, 30, 10, 20, 30]
    for value in values:
        bag.add(value)
    print(bag)

    print("\n# remove example 1")
    bag = Bag([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(bag)
    print(bag.remove(7), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)

    print("\n# count example 1")
    bag = Bag([1, 2, 3, 1, 2, 2])
    print(bag, bag.count(1), bag.count(2), bag.count(3), bag.count(4))

    print("\n# clear example 1")
    bag = Bag([1, 2, 3, 1, 2, 3])
    print(bag)
    bag.clear()
    print(bag)

    print("\n# equal example 1")
    bag1 = Bag([10, 20, 30, 40, 50, 60])
    bag2 = Bag([60, 50, 40, 30, 20, 10])
    bag3 = Bag([10, 20, 30, 40, 50])
    bag_empty = Bag()

    print(bag1, bag2, bag3, bag_empty, sep="\n")
    print(bag1.equal(bag2), bag2.equal(bag1))
    print(bag1.equal(bag3), bag3.equal(bag1))
    print(bag2.equal(bag3), bag3.equal(bag2))
    print(bag1.equal(bag_empty), bag_empty.equal(bag1))
    print(bag_empty.equal(bag_empty))
    print(bag1, bag2, bag3, bag_empty, sep="\n")

    bag1 = Bag([100, 200, 300, 200])
    bag2 = Bag([100, 200, 30, 100])
    print(bag1.equal(bag2))
