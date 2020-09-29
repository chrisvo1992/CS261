# Course: CS261 - Data Structures
# Student Name: Christopher Vo
# Assignment: 1
# Description: Will find the minimum and maximum values for any given StaticArray


from a1_include import *


def min_max(arr:StaticArray) -> ():
   """
   Function that takes an array as a parameter and will return the minimum
   and maximum values of the array in a tuple.
   """
   min, max = arr.get(0),arr.get(0) #sets first value of arr as both min and max variables

   for index in range(arr.size()):
       if arr.get(index) < min: #finds the minimum value
           min = arr.get(index)
       elif arr.get(index) > max: #finds the maximum value
           max = arr.get(index)

   return min, max

# BASIC TESTING
if __name__ == "__main__":

   # example 1
   arr = StaticArray(5)
   for i, value in enumerate([8, 7, 6, -5, 4]):
       arr[i] = value
   print(min_max(arr))


   # example 2
   arr = StaticArray(1)
   arr[0] = 100
   print(min_max(arr))

   # example 3
   arr = StaticArray(3)
   for i, value in enumerate([3, 3, 3]):
       arr[i] = value
   print(min_max(arr))
