# Course: CS261 - Data Structures
# Student Name: Christopher Vo
# Assignment: HW 1 Problem 7
# Description: Will sort the values in a StaticArray using insertion sort


from a1_include import *


def sa_sort(arr: StaticArray) -> None:
    """
    Takes a StaticArray as a parameter and will use insertion sort to sort the values
    of the StaticArray. It will change its original value without creating a new StaticArray
    """
    for i in range(1, arr.size()):
        key = arr.get(i)
        j = i - 1
        while j >= 0 and key < arr.get(j): #will go through array and find sort in ascending order
            arr.set(j + 1, arr.get(j))
            j -= 1
        arr.set(j + 1, key)

    return


# BASIC TESTING
if __name__ == "__main__":

    # example 1
    test_cases = (
        [1, 10, 2, 20, 3, 30, 4, 40, 5],
        ['zebra2', 'apple', 'tomato', 'apple', 'zebra1'],
        [(1, 1), (20, 1), (1, 20), (2, 20)]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        sa_sort(arr)
        print(arr)
