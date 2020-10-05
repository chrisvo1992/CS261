# Course: CS261 - Data Structures
# Student Name: Christopher Vo
# Assignment: HW 1 Problem 5
# Description: Function will create a StaticArray from values that are either increasing
#or decreasing from a specifies start and end points


from a1_include import *


def sa_range(start: int, end: int) -> StaticArray:
    """
    Takes a start and end int parameter. Will return a StaticArray that has values
    containing all the values between start and end(inclusively).
    """
    arr = StaticArray(abs(start-end) + 1)
    i = 0
    if start < end: #if your array is increasing
        arr.set(i, start)
        while start != end:
            start += 1
            i += 1
            arr.set(i, start)

    else: #if your array is decreasing
        arr.set(i, start)
        while start > end:
            i += 1
            start -= 1
            arr.set(i, start)

    return arr


# BASIC TESTING
if __name__ == "__main__":

    # example 1
    cases = [
        (1, 3), (-1, 2), (0, 0), (0, -3),
        (-105, -99), (-99, -105)]
    for start, end in cases:
        print(start, end, sa_range(start, end))
