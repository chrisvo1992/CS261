# Course: CS261 - Data Structures
# Student Name: Christopher Vo
# Assignment: HW 1 Problem 8
# Description: A function that returns removes all duplicate values from a StaticArray
#and will return a new StaticArray without duplicates.


from a1_include import *


def remove_duplicates(arr: StaticArray) -> StaticArray:
    """
    This function takes a StaticArray as parameter and will return a new StaticArray that
    removes duplicate values from the original array.
    """

    count = 0

    if arr.size() == 1: #if there is only 1 value in the StaticArray
        new_array = StaticArray(1)
        new_array.set(count, arr.get(0))
        return new_array

    #before you make a new StaticArray you must find the number of original values without duplicates
    for index in range(0, arr.size() - 1):
        if arr.get(index) != arr.get(index + 1):
            count += 1
    count += 1

    new_array = StaticArray(count)

    i = 0
    for index in range(0, arr.size() - 1):
        if arr.get(index) != arr.get(index + 1): #compares values ahead of the current index
            new_array.set(i, arr.get(index))
            i += 1
    new_array.set(i, arr.get(arr.size() - 1)) #gets the last value

    return new_array


# BASIC TESTING
if __name__ == "__main__":

    # example 1
    test_cases = (
        [1], [1, 2], [1, 1, 2], [1, 20, 30, 40, 500, 500, 500],
        [5, 5, 5, 4, 4, 3, 2, 1, 1], [1, 1, 1, 1, 2, 2, 2, 2]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        print(remove_duplicates(arr))
    print(arr)
