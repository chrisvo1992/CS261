# Course: CS261 - Data Structures
# Student Name: Christopher Vo
# Assignment: HW 3
# Description:


class SLLException(Exception):
    """
    Custom exception class to be used by Singly Linked List
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class SLNode:
    """
    Singly Linked List Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """

    def __init__(self, value: object) -> None:
        self.next = None
        self.value = value


class LinkedList:
    def __init__(self, start_list=None):
        """
        Initializes a new linked list with front and back sentinels
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.head = SLNode(None)
        self.tail = SLNode(None)
        self.head.next = self.tail

        # populate SLL with initial values (if provided)
        # before using this feature, implement add_back() method
        if start_list is not None:
            for value in start_list:
                self.add_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'SLL ['
        if self.head.next != self.tail:
            cur = self.head.next.next
            out = out + str(self.head.next.value)
            while cur != self.tail:
                out = out + ' -> ' + str(cur.value)
                cur = cur.next
        out = out + ']'
        return out

    def length(self) -> int:
        """
        Return the length of the linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        length = 0
        cur = self.head
        while cur.next != self.tail:
            cur = cur.next
            length += 1
        return length

    def is_empty(self) -> bool:
        """
        Return True is list is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.head.next == self.tail

    # ------------------------------------------------------------------ #

    def add_front(self, value: object) -> None:
        """
        TODO: Write this implementation
        """
        node = SLNode(value)

        if self.head.next == self.tail:
            self.head.next = node
            node.next = self.tail
            return

        temp = self.head.next
        self.head.next = node
        node.next = temp

    def add_back(self, value: object) -> None:
        """
        TODO: Write this implementation
        """
        node = SLNode(value)

        if self.head.next == self.tail:
            self.head.next = node
            node.next = self.tail
            return

        current = self.head.next

        for i in range(0, self.length()):
            if current.next.value is None:
                current.next = node
                node.next = self.tail
            current = current.next

    def insert_at_index(self, index: int, value: object) -> None:
        """
        TODO: Write this implementation
        """
        if index < 0 or index > self.length():
            raise SLLException

        node = SLNode(value)

        if index == 0 and self.length() == 0:
            self.head.next = node
            node.next = self.tail
            return

        if index == 0:
            current = self.head.next
            self.head.next = node
            node.next = current
            return

        current = self.head.next
        previous = None
        position = 0

        while position != index:
            previous = current
            current = current.next
            position += 1

        previous.next = node
        node.next = current

    def remove_front(self) -> None:
        """
        TODO: Write this implementation
        """
        if self.is_empty():
            raise SLLException

        head = self.head.next
        new_head = head.next
        self.head.next = new_head

    def remove_back(self) -> None:
        """
        TODO: Write this implementation
        """
        if self.length() == 0:
            raise SLLException

        if self.length() == 1:
            self.remove_front()
            return

        current = self.head.next
        previous = None
        for i in range(self.length()):
            if current.next.value is None:
                previous.next = current.next
            previous = current
            current = current.next

    def remove_at_index(self, index: int) -> None:
        """
        TODO: Write this implementation
        """
        if index < 0 or index > self.length():
            raise SLLException

        if index == 0:
            self.remove_front()
            return

        current = self.head.next
        previous = None

        for i in range(index):
            previous = current
            current = current.next

        if current.value == None:
            raise SLLException

        previous.next = current.next

    def get_front(self) -> object:
        """
        TODO: Write this implementation
        """
        if self.length() == 0:
            raise SLLException

        return self.head.next.value

    def get_back(self) -> object:
        """
        TODO: Write this implementation
        """
        if self.length() == 0:
            raise SLLException

        current = self.head.next
        for i in range(self.length() - 1):
            current = current.next

        return current.value

    def remove(self, value: object) -> bool:
        """
        TODO: Write this implementation
        """
        if self.length() == 0:
            return False


        current = self.head.next
        if current.value == value:
            temp = current.next
            self.head.next = temp
            return True

        previous = None
        for i in range(self.length()):
            if current.value == value:
                previous.next = current.next
                return True

            previous = current
            current = current.next

        return False

    def count(self, value: object) -> int:
        """
        TODO: Write this implementation
        """
        if self.length() == 0:
            return 0

        current = self.head.next
        counter = 0
        for i in range(self.length()):
            if current.value == value:
                counter += 1
            current = current.next

        return counter

    def slice(self, start_index: int, size: int) -> object:
        """
        TODO: Write this implementation
        """
        if self.length() == 0 or size > self.length() or start_index < 0 or start_index + size > self.length() \
                or size < 0 or start_index == self.length():
            raise SLLException

        new_list = LinkedList()

        current = self.head.next

        for i in range(start_index):
            current = current.next

        for i in range(size):
            new_list.add_back(current.value)
            current = current.next

        return new_list
