# Course: CS261 - Data Structures
# Student Name: Christopher Vo
# Assignment: HW 1 Problem 3
# Description: Reverses a the orders of the values in a StaticArray


from a1_include import *


def reverse(arr: StaticArray) -> None:
    """
    This function takes a StaticArray as a parameter and will reverse the values
    in the StaticArray. This does not create new StaticArray.
    """
    length = arr.size()
    for i in range(int(length / 2)): #reverses the order
        holder = arr.get(i) #place holder
        arr.set(i, arr.get(length - i - 1)) #set first value as last value
        arr.set(length - i - 1, holder) #set last value as first value

    return

# BASIC TESTING
if __name__ == "__main__":

    # example 1
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    reverse(arr)
    print(arr)
    reverse(arr)
    print(arr)
