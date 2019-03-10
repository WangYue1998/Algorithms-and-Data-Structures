"""
# Project 4
# Name: Yue Wang
# PID: A54267282
"""

class Stack:
    """
    Stack class
    """
    def __init__(self, capacity=2):
        """
        DO NOT MODIFY
        Creates an empty Stack with a fixed capacity
        :param capacity: Initial size of the stack. Default size 2.
        """
        self.capacity = capacity
        self.data = [None] * self.capacity
        self.size = 0

    def __str__(self):
        """
        DO NOT MODIFY
        Prints the values in the stack from bottom to top. Then, prints capacity.
        :return: string
        """
        if self.size == 0:
            return "Empty Stack"

        output = []
        for i in range(self.size):
            output.append(str(self.data[i]))
        return "{} Capacity: {}".format(output, str(self.capacity))

    def __eq__(self, stack2):
        """
        DO NOT MODIFY
        Checks if two stacks are equivalent to each other. Checks equivalency of data and capacity
        :return: True if equal, False if not
        """
        if self.capacity != stack2.capacity:
            return False

        count = 0
        for item in self.data:
            if item != stack2.data[count]:
                return False
            count += 1

        return True

    def stack_size(self):
        '''
        Time complexity: O(1)
        Space complexity: O(1)
        :return: Returns the current number of items in the stack.
        '''
        return self.size

    def is_empty(self):
        '''
        Time complexity: O(1)
        Space complexity: O(1)
        :return:Returns True if the stack is empty, False if not.
        '''
        return self.size == 0

    def top(self):
        '''
        Time complexity: O(1)
        Space complexity: O(1)
        :return:Returns the top item from the stack, None if the stack is empty. Does NOT remove the top item.
        '''
        if self.is_empty():
            return None
        return self.data[self.size-1]  # the last item in the list

    def push(self, val):
        '''
        Time complexity: O(1)*
        Space complexity: O(1)*
        :param val: Adds val to the top of the stack
        :return: returns nothing
        '''
        if self.size == self.capacity:  # not enough room
            self.grow()  # so double capacity
        self.data[self.size] = val
        self.size += 1

    def pop(self):
        '''
        Time complexity: O(1)*
        Space complexity: O(1)*
        :return: Removes the top item from stack by setting it back to None
        and returns the top item from the stack. Returns None if empty.
        '''
        if self.is_empty():
            return None
        lastitem = self.data[self.size-1]
        self.data[self.size-1] = None
        self.size = self.size-1
        self.shrink()
        return lastitem  # remove last item from list
       
    def grow(self):
        '''
        Time complexity: O(N)
        Space complexity: O(N)
        :return: Resize the stack to be 2 times its previous size when stack size equals capacity.
        Returns nothing.
        '''
        newstack = [None] * (self.capacity*2)  # new (bigger) array
        for k in range(self.size):  # for each existing value
            newstack[k] = self.data[k]
        self.data = newstack  # use the bigger array
        self.capacity = self.capacity*2

    def shrink(self):
        '''
        Time complexity: O(N)
        Space complexity: O(N)
        :return: Resize the stack to be half its current size
        when stack size is less than or equal to half its capacity.
         Note that stack capacity should never be below 2. Returns nothing.
        '''
        halfcapacity = self.capacity //2
        if self.size <= halfcapacity and self.capacity != 2:
            newstack = [None] * (halfcapacity)  # new (shrink) array
            for k in range(self.size):  # for each existing value
                newstack[k] = self.data[k]
            self.data = newstack  # use the bigger array
            self.capacity = self.capacity //2


def reverse(stack):
    '''
    Time complexity: O(N)
    Space complexity: O(N)
    :param stack: Reverse the order of the given stack, stack.
    :return:  Returns the reversed stack.
    '''
    new_stack = Stack()
    while not stack.is_empty():
        new_stack.push(stack.pop())
    return new_stack
    

def replace(stack, old, new):
    '''
    Time complexity: O(N)
    Space complexity: O(N)
    :param stack: the given stack
    :param old: Replace all instances of the integer value old
    :param new:  stack with the integer value new.
    :return: Return the stack with the replaced values.
    '''
    new_stack = Stack()
    while not stack.is_empty():
        value = stack.pop()
        if value == old :
            value = new
        new_stack.push(value)
    stack = reverse(new_stack)
    return stack
