# Course: CS261 - Data Structures
# Student Name: Christopher VO
# Assignment: Assignment 2
# Description: Dynamic Array class that has multiple methods to add,remove,resize,
#merge, or slice inner StaticArray member
# Last revised: 10/12/2020


from static_array import *


class DynamicArrayException(Exception):
    """
    Custom exception class to be used by Dynamic Array
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class DynamicArray:
    def __init__(self, start_array=None):
        """
        Initialize new dynamic array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.size = 0
        self.capacity = 4
        self.first = 0  # do not use / change this value
        self.data = StaticArray(self.capacity)

        # populate dynamic array with initial values (if provided)
        # before using this feature, implement append() method
        if start_array is not None:
            for value in start_array:
                self.append(value)

    def __str__(self) -> str:
        """
        Return content of dynamic array in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "DYN_ARR Size/Cap: "
        out += str(self.size) + "/" + str(self.capacity) + ' ['
        out += ', '.join([str(self.data[_]) for _ in range(self.size)])
        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True is array is empty / False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.size == 0

    def length(self) -> int:
        """
        Return number of elements stored in array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.size

    def resize(self, new_capacity: int) -> None:
        """
        This method will change the self.capacity variable with a new_capacity parameter.
        If the parameter is less than 0 or less than the current size then return nothing.
        A new StaticArray will be created that is twice the size of current array then
        all elements will be copied into the new array and continue appending there.
        """
        if new_capacity < 0 or new_capacity <= self.size:
            return

        else:
            new_data = StaticArray(new_capacity)  # Create a new StaticArray 2x size of current array
            if new_capacity < self.data.size():  # if new_capacity is < the capacity of current array
                for i in range(new_data.size()):
                    new_data.set(i, self.data.get(i)) #copy all elements into new array
            else:
                for i in range(self.data.size()):
                    new_data.set(i, self.data.get(i))
            self.data = new_data  # change references to new array
            self.capacity = new_capacity

    def append(self, value: object) -> None:
        """
        This function takes a value as a parameter and will add this value to the current
        array. If the current size of array has met its capacity this method will call
        resize() and double the current size and then append new value to array.
        """
        if self.size == self.capacity:
            self.resize(self.capacity * 2)  # doubles the capacity of current array

        self.data.set(self.size, value)
        self.size += 1  # increment size each time this function is called

    def insert_at_index(self, index: int, value: object) -> None:
        """
        This function will add a value into the array at a specified index. If
        the index is invalid will raise DynamicArrayException. If the size of
        array is at capacity resize() will be called to double capacity. This
        will shift all elements to the right after the specified index then
        insert new value at index location.
        """
        if index < 0 or index > self.size:
            raise DynamicArrayException

        if self.size == self.capacity:
            self.resize(self.capacity * 2)

        for i in range(self.size - 1, index - 1, -1): #shift all elements to the right of the index
            self.data.set(i + 1, self.data.get(i))

        self.data.set(index, value) #once all elements are moved, insert new value in index
        self.size += 1

    def get_at_index(self, index: int) -> object:
        """
        This function will return the value at a specified index. If index is invalid will
        raise DynamicArrayException.
        """
        if index < 0 or index >= self.size:
            raise DynamicArrayException

        return self.data.get(index)

    def remove_at_index(self, index: int) -> None:
        """
        This function will remove a value at a specified index. Before removing item this
        will check if the current size is less than 25% capacity. If it is then the
        capacity will be changed to double the current size of array but will stay above 10.
        Will shift all elements to the left at index.
        """
        if index < 0 or index >= self.size:
            raise DynamicArrayException

        if (self.size / self.capacity) < 0.25 and self.size >= 5: #checks if size is less than 25% capacity
            self.resize(self.size * 2)

        elif (self.size / self.capacity) < 0.25 and self.size < 5 and self.size > 1: #makes sure capacity is at least 10
            self.resize(10)

        for i in range(index, self.size - 1): #shift all elements to the left
            self.data.set(i, self.data.get(i + 1))

        self.size -= 1

    def slice(self, start_index: int, quantity: int) -> object:
        """
        This function is return all values between 2 specified locations. Has 2 parameters:
        first the starting index where to copy values then the quantity after the starting index.
        If start_index or quantity are invalid raise DynamicArrayException.
        """
        if start_index < 0 or start_index >= self.size or quantity < 0 or start_index + quantity > self.size:
            raise DynamicArrayException

        new_data = DynamicArray()
        try:
            for i in range(start_index, start_index + quantity): #copy from start_index to end index
                new_data.append(self.data.get(i))

        except DynamicArrayException:
            raise DynamicArrayException

        return new_data

    def merge(self, second_da: object) -> None:
        """
        This function will combine all values of another array to current array.
        This will not change order of 2nd array.
        """
        for i in range(second_da.length()):
            self.append(second_da.get_at_index(i)) #add all values of 2nd array to current array

    def map(self, map_func) -> object:
        """
        This function takes a function as a parameter and will use the function
        on all values of current array. A values will be returned in a new array.
        """
        new_data = DynamicArray()

        for i in range(self.size):
            new_data.append(map_func(self.get_at_index(i)))

        return new_data

    def filter(self, filter_func) -> object:
        """
        This function takes a function as a parameter and will use the function
        on all values of current array. A values will be returned in a new array.
        Will only return values that have True boolean values from filter_func.
        """
        new_data = DynamicArray()
        for i in range(self.size):
            if filter_func(self.get_at_index(i)) == True: #only copy values with True boolean values
                new_data.append(self.get_at_index(i))

        return new_data


    def reduce(self, reduce_func, initializer=None) -> object:
        """
        This function will return the results of a reduce_func on
        all values of current array.
        """
        result = 0
        if self.size == 0:
            return initializer

        if initializer is None: #if no initializer is provided the first value of array will take its place
            result = self.get_at_index(0)
            for i in range(1, self.size):
                result += reduce_func(0, self.get_at_index(i)) #only changes y value

            return result

        result += initializer #if initializer is provided
        for i in range(0, self.size):
            result += reduce_func(0, self.get_at_index(i)) #only changes y value

        return result



# BASIC TESTING
if __name__ == "__main__":

    print("\n# resize - example 1")
    da = DynamicArray()
    print(da.size, da.capacity, da.data)
    da.resize(8)
    print(da.size, da.capacity, da.data)
    da.resize(2)
    print(da.size, da.capacity, da.data)
    da.resize(0)
    print(da.size, da.capacity, da.data)

    print("\n# resize - example 2")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8])
    print(da)
    da.resize(20)
    print(da)
    da.resize(4)
    print(da)

    print("\n# append - example 1")
    da = DynamicArray()
    print(da.size, da.capacity, da.data)
    da.append(1)
    print(da.size, da.capacity, da.data)
    print(da)

    print("\n# append - example 2")
    da = DynamicArray()
    for i in range(9):
        da.append(i + 101)
        print(da)

    print("\n# append - example 3")
    da = DynamicArray()
    for i in range(600):
        da.append(i)
    print(da.size)
    print(da.capacity)

    print("\n# insert_at_index - example 1")
    da = DynamicArray([100])
    print(da)
    da.insert_at_index(0, 200)
    da.insert_at_index(0, 300)
    da.insert_at_index(0, 400)
    print(da)
    da.insert_at_index(3, 500)
    print(da)
    da.insert_at_index(1, 600)
    print(da)

    print("\n# insert_at_index example 2")
    da = DynamicArray()
    try:
        da.insert_at_index(-1, 100)
    except Exception as e:
        print("Exception raised:", type(e))
    da.insert_at_index(0, 200)
    try:
        da.insert_at_index(2, 300)
    except Exception as e:
        print("Exception raised:", type(e))
    print(da)

    print("\n# insert at index example 3")
    da = DynamicArray()
    for i in range(1, 10):
        index, value = i - 4, i * 10
        try:
            da.insert_at_index(index, value)
        except Exception as e:
            print("Can not insert value", value, "at index", index)
    print(da)

    print("\n# get_at_index - example 1")
    da = DynamicArray([10, 20, 30, 40, 50])
    print(da)
    for i in range(4, -1, -1):
        print(da.get_at_index(i))

    print("\n# get_at_index example 2")
    da = DynamicArray([100, 200, 300, 400, 500])
    print(da)
    for i in range(-1, 7):
        try:
            print("Index", i, ": value", da.get_at_index(i))
        except Exception as e:
            print("Index", i, ": exception occurred")

    print("\n# remove_at_index - example 1")
    da = DynamicArray([10, 20, 30, 40, 50, 60, 70, 80])
    print(da)
    da.remove_at_index(0)
    print(da)
    da.remove_at_index(6)
    print(da)
    da.remove_at_index(2)
    print(da)

    # remove_at_index - example 2
    da = DynamicArray([1024])
    print(da)
    for i in range(17):
        da.insert_at_index(i, i)
    print(da.size, da.capacity)
    for i in range(16, -1, -1):
        da.remove_at_index(0)
    print(da)

    print("\n# remove_at_index - example 3")
    da = DynamicArray()
    print(da.size, da.capacity)
    [da.append(1) for i in range(100)]          # step 1 - add 100 elements
    print(da.size, da.capacity)
    [da.remove_at_index(0) for i in range(68)]  # step 2 - remove 69 elements
    print(da.size, da.capacity)
    da.remove_at_index(0)                       # step 3 - remove 1 element
    print(da.size, da.capacity)
    da.remove_at_index(0)                       # step 4 - remove 1 element
    print(da.size, da.capacity)
    [da.remove_at_index(0) for i in range(14)]  # step 5 - remove 14 elements
    print(da.size, da.capacity)
    da.remove_at_index(0)                       # step 6 - remove 1 element
    print(da.size, da.capacity)
    da.remove_at_index(0)                       # step 7 - remove 1 element
    print(da.size, da.capacity)

    for i in range(14):
        print("Before remove_at_index(): ", da.size, da.capacity, end="")
        da.remove_at_index(0)
        print(" After remove_at_index(): ", da.size, da.capacity)


    print("\n# remove at index - example 4")
    da = DynamicArray([1, 2, 3, 4, 5])
    print(da)
    for _ in range(5):
        da.remove_at_index(0)
        print(da)

    print("\n# slice example 1")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8, 9])
    da_slice = da.slice(1, 3)
    print(da, da_slice, sep="\n")
    da_slice.remove_at_index(0)
    print(da, da_slice, sep="\n")

    print("\n# slice example 2")
    da = DynamicArray([10, 11, 12, 13, 14, 15, 16])
    print("SOUCE:", da)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1), (6, -1)]
    for i, cnt in slices:
        print("Slice", i, "/", cnt, end="")
        try:
            print(" --- OK: ", da.slice(i, cnt))
        except:
            print(" --- exception occurred.")

    print("\n# merge example 1")
    da = DynamicArray([1, 2, 3, 4, 5])
    da2 = DynamicArray([10, 11, 12, 13])
    print(da)
    da.merge(da2)
    print(da)

    print("\n# merge example 2")
    da = DynamicArray([1, 2, 3])
    da2 = DynamicArray()
    da3 = DynamicArray()
    da.merge(da2)
    print(da)
    da2.merge(da3)
    print(da2)
    da3.merge(da)
    print(da3)

    print("\n# map example 1")
    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    print(da.map(lambda x: x ** 2))


    print("\n# map example 2")
    def double(value):
        return value * 2

    def square(value):
        return value ** 2

    def cube(value):
        return value ** 3

    def plus_one(value):
        return value + 1

    da = DynamicArray([plus_one, double, square, cube])
    for value in [1, 10, 20]:
        print(da.map(lambda x: x(value)))


    print("\n# filter example 1")
    def filter_a(e):
        return e > 10

    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    result = da.filter(filter_a)
    print(result)
    print(da.filter(lambda x: (10 <= x <= 20)))


    print("\n# filter example 2")
    def is_long_word(word, length):
        return len(word) > length

    da = DynamicArray("This is a sentence with some long words".split())
    print(da)
    for length in [3, 4, 7]:
        print(da.filter(lambda word: is_long_word(word, length)))


    print("\n# reduce example 1")
    values = [100, 5, 10, 15, 20, 25]
    da = DynamicArray(values)
    print(da)
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))

    print("\n# reduce example 2")
    da = DynamicArray([100])
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))
    da.remove_at_index(0)
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))
