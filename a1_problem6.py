# Course: CS261 - Data Structures
# Student Name: Christopher Vo
# Assignment: Hw 1 Problem 6
# Description: This function will check if a StaticArray has values that are sorted or not
#If the values are in ascending order the function will return 1, if descending order return 2,
# and if neither apply will return 0


from a1_include import *


def is_sorted(arr: StaticArray) -> int:
    """
    This function takes a StaticArray as a parameter and will check to see if the values
    are in ascending order, descending order, or not in any order. If in ascending order
    this will return 1, if in descending order will return 2, if neither order will return 0.
    """
    ascending = True
    while ascending == True: #first checks if values are in ascending order
        for item in range(0, arr.size()-1):
            if arr.get(item) < arr.get(item + 1):
                ascending = True
            else: #if not in ascending order will break out of this while loop and change ascending
                ascending = False
                break
        if ascending == True: #if items are in ascending order return 1
            return 1

    while ascending == False: #checks if values are in descending order
        for item in range(0, arr.size()-1):
            if arr.get(item) > arr.get(item + 1):
                ascending = False
            else: #if not in descending order will change ascending value to None and break
                ascending = None
                break
        if ascending == False: #if items are in descending order return 2
            return 2

    if ascending == None: #if values are neither ascending or descending order
        return 0



# BASIC TESTING
if __name__ == "__main__":

    # example 1
    test_cases = (
        [-100, -8, 0, 2, 3, 10, 20, 100],
        ['A', 'B', 'Z', 'a', 'z'],
        ['Z', 'T', 'K', 'A', '1'],
        [1, 3, -10, 20, -30, 0],
        [-10, 0, 0, 10, 20, 30],
        [100, 90, 0, -90, -200],
        ['apple']
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print('Result:', is_sorted(arr), arr)
