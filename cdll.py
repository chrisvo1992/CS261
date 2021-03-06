# Course: CS261 - Data Structures
# Student Name: christopher vo
# Assignment: hw 3
# Description:


class CDLLException(Exception):
    """
    Custom exception class to be used by Circular Doubly Linked List
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class DLNode:
    """
    Doubly Linked List Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """

    def __init__(self, value: object) -> None:
        self.next = None
        self.prev = None
        self.value = value


class CircularList:
    def __init__(self, start_list=None):
        """
        Initializes a new linked list with sentinel
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.sentinel = DLNode(None)
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel

        # populate CDLL with initial values (if provided)
        # before using this feature, implement add_back() method
        if start_list is not None:
            for value in start_list:
                self.add_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'CDLL ['
        if self.sentinel.next != self.sentinel:
            cur = self.sentinel.next.next
            out = out + str(self.sentinel.next.value)
            while cur != self.sentinel:
                out = out + ' <-> ' + str(cur.value)
                cur = cur.next
        out = out + ']'
        return out

    def length(self) -> int:
        """
        Return the length of the linked list

        This can also be used as troubleshooting method. This method works
        by independently measuring length during forward and backward
        traverse of the list and return the length if results agree or error
        code of -1 or -2 if thr measurements are different.

        Return values:
        >= 0 - length of the list
        -1 - list likely has an infinite loop (forward or backward)
        -2 - list has some other kind of problem

        DO NOT CHANGE THIS METHOD IN ANY WAY
        """

        # length of the list measured traversing forward
        count_forward = 0
        cur = self.sentinel.next
        while cur != self.sentinel and count_forward < 101_000:
            count_forward += 1
            cur = cur.next

        # length of the list measured traversing backwards
        count_backward = 0
        cur = self.sentinel.prev
        while cur != self.sentinel and count_backward < 101_000:
            count_backward += 1
            cur = cur.prev

        # if any of the result is > 100,000 -> list has a loop
        if count_forward > 100_000 or count_backward > 100_000:
            return -1

        # if counters have different values -> there is some other problem
        return count_forward if count_forward == count_backward else -2

    def is_empty(self) -> bool:
        """
        Return True is list is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.sentinel.next == self.sentinel

    # ------------------------------------------------------------------ #

    def add_front(self, value: object) -> None:
        """
        TODO: Write this implementation
        """
        node = DLNode(value)

        node.prev = self.sentinel
        node.next = self.sentinel.next
        self.sentinel.next = node
        node.next.prev = node

    def add_back(self, value: object) -> None:
        """
        TODO: Write this implementation
        """

        node = DLNode(value)

        current = self.sentinel.prev
        current.next = node
        node.next = self.sentinel
        node.prev = current
        self.sentinel.prev = node



    def insert_at_index(self, index: int, value: object) -> None:

        if index > self.length() or index < 0:
            raise CDLLException

        if self.is_empty():
            self.add_front(value)
            return

        if index == 0:
            self.add_front(value)
            return

        node = DLNode(value)

        current = self.sentinel
        for i in range(index):
            current = current.next

        current.next.prev = node
        node.next = current.next
        node.prev = current
        current.next = node



    def remove_front(self) -> None:
        """
        TODO: Write this implementation
        """
        if self.is_empty():
            raise CDLLException

        firstNode = self.sentinel.next
        firstNode.next.prev = self.sentinel
        self.sentinel.next = firstNode.next


    def remove_back(self) -> None:
        """
        TODO: Write this implementation
        """
        if self.is_empty():
            raise CDLLException

        lastNode = self.sentinel.prev
        lastNode.prev.next = self.sentinel
        self.sentinel.prev = lastNode.prev

    def remove_at_index(self, index: int) -> None:
        """
        TODO: Write this implementation
        """
        if self.is_empty() or index < 0 or index > self.length():
            raise CDLLException

        if index == 0:
            self.remove_front()
            return

        current = self.sentinel.next
        for i in range(index):
            current = current.next

        if current.value == None:
            raise CDLLException

        current.prev.next = current.next
        current.next.prev = current.prev


    def get_front(self) -> object:
        """
        TODO: Write this implementation
        """
        if self.is_empty():
            raise CDLLException
        return self.sentinel.next.value

    def get_back(self) -> object:
        """
        TODO: Write this implementation
        """
        if self.is_empty():
            raise CDLLException
        return self.sentinel.prev.value

    def remove(self, value: object) -> bool:
        """
        TODO: Write this implementation
        """
        if self.is_empty():
            raise CDLLException

        current = self.sentinel.next
        if current.value == value:
            temp = current.next
            self.sentinel.next = temp
            temp.prev = self.sentinel
            return True

        previous = None

        for i in range(self.length()):
            if current.value == value:
                previous.next = current.next
                current.next.prev = previous
                return True
            previous = current
            current = current.next

        return False


    def count(self, value: object) -> int:
        """
        TODO: Write this implementation
        """
        if self.is_empty():
            return 0

        current = self.sentinel.next
        counter = 0
        for i in range(self.length()):
            if current.value == value:
                counter += 1
            current = current.next
        return counter

    def swap_pairs(self, index1: int, index2: int) -> None:
        """
        TODO: Write this implementation
        """
        if index1 < 0 or index1 >= self.length() or index2 < 0 or index2 >= self.length():
            raise CDLLException

        if index1 == index2:
            return

        current1 = self.sentinel.next
        prev1 = None
        current2 = self.sentinel.next
        prev2 = None

        for i in range(index1):
            prev1 = current1
            current1 = current1.next
        if index1 == 0:
            prev1 = self.sentinel
        forward1 = current1.next

        for i in range(index2):
            prev2 = current2
            current2 = current2.next
        if index2 == 0:
            prev2 = self.sentinel

        forward2 = current2.next

        if prev1 != current2 and prev2 != current1:
            current1.next = forward2
            forward2.prev = current1

            current2.next = forward1
            forward1.prev = current2

            current1.prev = prev2
            current2.prev = prev1

            prev1.next = current2
            prev2.next = current1
            return

        if index1 < index2:
            current1.next = forward2
            forward2.prev = current1

            current2.next = current1
            current1.prev = current2

            prev1.next = current2
            current2.prev = prev1

        elif index1 > index2:
            current2.next = forward1
            forward1.prev = current2

            current1.next = current2
            current2.prev = current1

            prev2.next = current1
            current1.prev = prev2

    def reverse(self) -> None:
        """
        TODO: Write this implementation
        """
        if self.is_empty():
            return

        index1, index2 = 0, self.length()-1
        for i in range(int(self.length()/2)):
            self.swap_pairs(index1, index2)
            index1 += 1
            index2 -= 1

    def sort(self) -> None:
        """
        TODO: Write this implementation
        """
        if self.is_empty():
            return


        for i in range(self.length()-1):
            for j in range(0, self.length()-i-1):
                if self.get_value(j) > self.get_value(j+1):
                    self.swap_pairs(j, j+1)


    def get_value(self, index):
        """
        helper function for sort method. Will return the value at a specified index
        """
        current = self.sentinel.next
        for i in range(index):
            current = current.next

        return current.value


    def rotate(self, steps: int) -> None:
        """
        TODO: Write this implementation
        """
        if steps == 0 or steps == self.length() or self.is_empty():
            return

        if steps > self.length():
            steps = steps % self.length()

        if steps > 0 and steps < self.length():
            current = self.sentinel.prev
            for i in range(steps-1):
                current = current.prev

            endNode = self.sentinel.prev
            firstNode = self.sentinel.next

            endNode.next = firstNode
            firstNode.prev = endNode

            prev = current.prev
            current.prev = self.sentinel
            self.sentinel.prev = prev
            self.sentinel.next = current
            prev.next = self.sentinel

        if abs(steps) > self.length():
            steps = abs(steps) % self.length()
            steps = steps * -1

        if steps < 0 and abs(steps) < self.length():
            current = self.sentinel.next
            steps = abs(steps)
            endNode = self.sentinel.prev
            firstNode = self.sentinel.next

            for i in range(steps):
                current = current.next

            endNode.next = firstNode
            firstNode.prev = endNode
            prev = current.prev
            current.prev = self.sentinel
            self.sentinel.prev = prev
            self.sentinel.next = current
            prev.next = self.sentinel



    def remove_duplicates(self) -> None:
        """
        TODO: Write this implementation
        """
        pass

    def odd_even(self) -> None:
        """
        TODO: Write this implementation
        """
        pass


if __name__ == '__main__':


    print('\n# remove_duplicates example 1')
    test_cases = (
    [1, 2, 3, 4, 5], [1, 1, 1, 1, 1],
    [], [1], [1, 1], [1, 1, 1, 2, 2, 2],
    [0, 1, 1, 2, 3, 3, 4, 5, 5, 6],list("abccd"),list("005BCDDEEFI")
    )

    print(list("032hfsha"))
    for case in test_cases:
        lst = CircularList(case)
        print('INPUT :', lst)
        lst.remove_duplicates()
        print('OUTPUT:', lst)
    """
    # print('\n# odd_even example 1')
    test_cases = (
    [1, 2, 3, 4, 5], list('ABCDE'),
    [], [100], [100, 200], [100, 200, 300],
    [100, 200, 300, 400],
    [10, 'A', 20, 'B', 30, 'C', 40, 'D', 50, 'E'] )
    #
    # for case in test_cases:
    #     lst = CircularList(case)
    #     print('INPUT :', lst)
    #     lst.odd_even()
    #     print('OUTPUT:', lst)
"""