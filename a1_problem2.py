# Course: CS261 - Data Structures
# Student Name: Christopher Vo
# Assignment: HW 1 Problem 2
# Description: A function named fizz_buzz() will take a StaticArray as a parameter and
#return a new StaticArray. If the values are divisible by 3 the new StaticArray will show
#fizz, if the value is divisible by 5 then it will show buzz, and if it is divisible by
#3 & 5 it will show fizzbuzz. If nether conditions apply it will be left unchanged.


from a1_include import *


def fizz_buzz(arr: StaticArray) -> StaticArray:
    """
    Takes a StaticArray object as a parameter. This function will create a new
    StaticArray that is the same size as the parameter. Every value that is divisible by
    3 will be changed to fizz, values divisible by 5 will be changed to buzz, and values
    divisible by 3 and 5 will be changed to fizzbuzz in the new StaticArray. If none
    conditions apply the value will be unchanged. The new array will be returned.
    """
    new_arr = StaticArray(arr.size()) #creating new StaticArray with same size as parameter

    for index in range(arr.size()):
        if arr.get(index) % 3 == 0 and arr.get(index) % 5 != 0: #if only divisible by 3
            new_arr[index] = "fizz"
        elif arr.get(index) % 5 == 0 and arr.get(index) % 3 != 0: #if only divisible by 5
            new_arr[index] = "buzz"
        elif arr.get(index) % 5 == 0 and arr.get(index) % 3 == 0:#if  divisible by 3 & 5
            new_arr[index] = "fizzbuzz"
        else: #if none of above conditions apply
            new_arr[index] = arr.get(index)

    return new_arr


# BASIC TESTING
if __name__ == "__main__":

    # example 1
    source = [_ for _ in range(-5, 20, 4)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(fizz_buzz(arr))
    print(arr)
