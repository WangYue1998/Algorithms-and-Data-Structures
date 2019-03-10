"""
# Project 5
# Name: Yue Wang
# PID: A54267282
"""

"""implement a circular queue.
A queue is an abstract data type where the first item in is the first item out.
A circular queue is one that uses an underlying list and uses modulo arithmetic
    to allow for reuse of space after enqueues and dequeues.
"""
class CircularQueue():
    # DO NOT MODIFY THESE METHODS
    def __init__(self, capacity=4):
        """
        Initialize the queue with an initial capacity
        :param capacity: the initial capacity of the queue
        """
        self.capacity = capacity
        self.size = 0
        self.data = [None] * capacity
        self.head = 0
        self.tail = 0


    def __eq__(self, other):
        """
        Defines equality for two queues
        :return: true if two queues are equal, false otherwise
        """
        if self.capacity != other.capacity:
            return False
        for i in range(self.capacity):
            if self.data[i] != other.data[i]:
                return False
        return self.head == other.head and self.tail == other.tail and self.size == other.size

    # -----------MODIFY BELOW--------------

    def __str__(self):
        '''
        This method is solely for development purposes for you and will not be tested.
        :return: the data in self.data
        '''
        if self.size == 0:
            return "Empty Stack"

        output = []
        for i in range(self.size):
            output.append(str(self.data[i]))
        return "{} Capacity: {}".format(output, str(self.capacity))

    def is_empty(self):
        """
        check if the queue is empty
        O(1) time complexity, O(1) space complexity
        :return: Returns whether or not is empty (bool)
        """
        return self.size == 0

    def __len__(self):
        """
        get the length of queue
        O(1) time complexity, O(1) space complexity
        :return: Returns the size of the queue
        """
        return self.size

    def first_value(self):
        """
        get the first value of queue
        O(n) time complexity, O(1) space complexity
        :return: Returns the front of the queue
        """
        if not self.is_empty():
            return self.data[self.head]
        return None

    def enqueue(self, val):
        """
        add the val to the queue
        O(1)* time complexity, O(1)* space complexity
        :param val: Add a number to the back of the queue
        :return: Return None
        """
        if self.size+1 == self.capacity:
            self.grow()  # double the array size
        #avail = (self.head + self.size) % len(self.data)
        self.data[self.tail] = val
        self.size += 1
        self.tail = (self.tail + 1) % self.capacity
        return None
        


    def dequeue(self):
        """
        delete the front value of queue
        O(1)* time complexity, O(1)* space complexity
        Remove an element from the front of a queue if not empty, do nothing otherwise
        :return: Return element popped
        """
        if not self.is_empty():
            answer = self.data[self.head]
            self.data[self.head] = None  # help garbage collection
            self.head = (self.head + 1) % self.capacity
            self.size -= 1
            if self.size <= self.capacity//4 and self.capacity > 4:
                self.shrink()
            return answer
        return None

    def grow(self):
        """
        double the capacity of queue
        O(n) time complexity, O(n) space complexity
        Moves the head to the front of the newly allocated list
        Doubles the capacity of the queue immediately when
            capacity is reached to make room for new elements
        :return: no return
        """
        old = self.data  # keep track of existing list
        self.capacity = self.capacity*2
        self.data = [None] * (self.capacity) # allocate list with new capacity
        walk = self.head
        for k in range(self.size):  # only consider existing elements
            self.data[k] = old[walk]  # intentionally shift indices
            walk = (1 + walk) % len(old)  # use old size as modulus
        self.head = 0  # front has been realigned

    def shrink(self):
        """
        half the capacity of queue
        Halves the capacity of the queue if the size is 1/4 of the capacity
        Capacity should never go below 4
        Moves the head to the front of the newly allocated list
        O(n) time complexity, O(n) space complexity
        :return: no return
        """
        old = self.data  # keep track of existing list
        self.capacity = self.capacity // 2
        self.data = [None] * (self.capacity)  # allocate list with new capacity
        walk = self.head
        for k in range(self.size):  # only consider existing elements
            self.data[k] = old[walk]  # intentionally shift indices
            walk = (1 + walk) % len(old)  # use old size as modulus
        self.head = 0  # front has been realigned
        self.tail = self.size
