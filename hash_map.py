# Course: CS261 - Data Structures
# Assignment: 5
# Student: Christopher Vo
# Description: Hash table class with the ability to clear, get, get keys, put, remove,resize,
#or table load functions


# Import pre-written DynamicArray and LinkedList classes
from a5_include import *


def hash_function_1(key: str) -> int:
    """
    Sample Hash function #1 to be used with A5 HashMap implementation
    DO NOT CHANGE THIS FUNCTION IN ANY WAY
    """
    hash = 0
    for letter in key:
        hash += ord(letter)
    return hash


def hash_function_2(key: str) -> int:
    """
    Sample Hash function #2 to be used with A5 HashMap implementation
    DO NOT CHANGE THIS FUNCTION IN ANY WAY
    """
    hash, index = 0, 0
    index = 0
    for letter in key:
        hash += (index + 1) * ord(letter)
        index += 1
    return hash


class HashMap:
    def __init__(self, capacity: int, function) -> None:
        """
        Init new HashMap based on DA with SLL for collision resolution
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.buckets = DynamicArray()
        for _ in range(capacity):
            self.buckets.append(LinkedList())
        self.capacity = capacity
        self.hash_function = function
        self.size = 0

    def __str__(self) -> str:
        """
        Return content of hash map t in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = ''
        for i in range(self.buckets.length()):
            list = self.buckets.get_at_index(i)
            out += str(i) + ': ' + str(list) + '\n'
        return out

    def clear(self) -> None:
        """
        Will clear all hash table elements
        """
        for i in range(self.capacity): #clears the bucket of all elements
            self.buckets.pop()

        for i in range(self.capacity): #create new empty bucket with same capacity
            self.buckets.append(LinkedList())

        self.size = 0

    def get(self, key: str) -> object:
        """
        Will return the value at the given key provided in parameter
        """

        hash_key = self.hash_function(key)
        index = hash_key % self.capacity
        bucket = self.buckets.get_at_index(index)
        if bucket.contains(key) is None: #if not found
            return None
        else:
            return bucket.contains(key).value



    def put(self, key: str, value: object) -> None:
        """
        This function takes a key and value as parameters and will insert the pair into the hash table.
        If a key already exists the value of that key will be updated without being removed.
        """
        hash_key = self.hash_function(key)
        index = hash_key % self.capacity

        l_list = self.buckets.get_at_index(index)
        if l_list.contains(key) is None: #if key is not found in list
            l_list.insert(key, value)
            self.size += 1
        else: #if key is found just update the value
            l_list.contains(key).value = value


    def remove(self, key: str) -> None:
        """
        This function takes a key as a parameter and will remove the node in the hash table
        """
        hash_key = self.hash_function(key)
        index = hash_key % self.capacity

        l_list = self.buckets.get_at_index(index)
        if l_list.contains(key) is None: #if not found
            return None
        else:
            l_list.remove(key)
            self.size -= 1

    def contains_key(self, key: str) -> bool:
        """
        This function takes a key as a parameter and will verify if the key exists in the hash table.
        Returns True if found and False is not
        """
        if self.size == 0:
            return False

        for i in range(self.buckets.length()):
            if self.buckets.get_at_index(i).contains(key) is not None:
                return True

        return False

    def empty_buckets(self) -> int:
        """
        This function will return the number of empty buckets in the hash table
        """
        counter = 0
        for i in range(self.buckets.length()):
            if self.buckets.get_at_index(i).length() == 0:
                counter += 1
        return counter

    def table_load(self) -> float:
        """
        Will calculate and return the table load of current hash table
        """
        return self.size / self.capacity

    def resize_table(self, new_capacity: int) -> None:
        """
        This function takes a new capacity as a parameter and will re organize elements in current hash table
        to the new hash table
        """
        if new_capacity < 1:
            return

        new_array = DynamicArray() #create new array to copy elements over
        for i in range(new_capacity):
            new_array.append(LinkedList())

        for i in range(self.buckets.length()): #traverse through whole current array
            l_list = self.buckets.get_at_index(i)
            if l_list is not None:
                iter = l_list.__iter__() #iterate through each node
                for node in iter:
                    hash_key = self.hash_function(node.key)
                    index = hash_key % new_capacity
                    bucket = new_array.get_at_index(index)
                    if bucket.contains(node.key) is None: #re-put all values with new hash_key into new array
                        bucket.insert(node.key, node.value)
                        bucket.size += 1

                    else:
                        bucket.contains(node.key).value = node.value

        self.buckets = new_array #change pointers
        self.capacity = new_capacity


    def get_keys(self) -> DynamicArray:
        """
        This function will return an array with only the keys in the hash table.
        """
        key_array = DynamicArray()

        for i in range(self.buckets.length()):
            l_list = self.buckets.get_at_index(i)
            if l_list is not None:
                iter = l_list.__iter__() #iterate through each node
                for node in iter:
                    key_array.append(node.key)
        return key_array
