########################################
# PROJECT: Binary Min Heap and Sort
# Author: Yue Wang
########################################

class BinaryMinHeap:
    # DO NOT MODIFY THIS CLASS #
    def __init__(self):
        """
        Creates an empty hash table with a fixed capacity
        """
        self.table = []


    def __eq__(self, other):
        """
        Equality comparison for heaps
        :param other: Heap being compared to
        :return: True if equal, False if not equal
        """
        if len(self.table) != len(other.table):
            return False
        for i in range(len(self.table)):
            if self.table[i] != other.table[i]:
                return False

        return True

    ###### COMPLETE THE FUNCTIONS BELOW ######

    def __str__(self):
        pass

    def get_size(self):
        """
        Returns the number of nodes currently in the Heap
        Time complexity: O(1)
        Space complexity: O(1)
        :return: number of nodes
        """
        return len(self.table)

    def parent(self, position):
        """
        Finds the parent of the node at index position
        Returns the index of the parent node
        Time complexity: O(1)
        Space complexity: O(1)
        :param position: index position
        :return: index of parent node
        """
        return (position-1)//2

    def left_child(self, position):
        """
        Finds the left child of the node at index position
        Returns the index of the left child node
        Time complexity: O(1)
        Space complexity: O(1)
        :param position: index position
        :return: the index of the left child node
        """
        return 2*position+1

    def right_child(self, position):
        """
        Finds the right child of the node at index position
        Returns the index of the right child node
        Time complexity: O(1)
        Space complexity: O(1)
        :param position: index position
        :return: index of the right child node
        """
        return 2*position+2

    def has_left(self, position):
        """
        Returns True if the node at index position has a left child, False otherwise
        Time complexity: O(1)
        Space complexity: O(1)
        :param position: index position
        :return: True or False
        """
        if self.left_child(position) < self.get_size():
            return True
        return False

    def has_right(self, position):
        """
        Returns True if the node at index position has a right child, False otherwise
        Time complexity: O(1)
        Space complexity: O(1)
        :param position: index position
        :return: True or False
        """
        if self.right_child(position) < self.get_size():
            return True
        return False

    def find(self, value):
        """
        Returns the index of the node with value
        Returns None if the value is not found in the heap
        Time complexity: O(n)
        Space complexity: O(1)
        :param value: value to find
        :return: index of the node with value
        """
        for i in range(self.get_size()):
            if self.table[i] == value:
                return i
        return None

    def heap_push(self, value):
        """
        Adds a node with the given value and adds it to the heap
        Duplicates are ignored
        Returns nothing
        Time complexity: O(nlog(n))*
        Space complexity: O(1)
        :param value: the value to added
        :return:
        """
        if self.find(value) is None:
            self.table.append(value)
            self.percolate_up(self.get_size()-1)

    def heap_pop(self, value):
        """
        Removes the node with the given value
        Time complexity: O(nlog(n))*
        Space complexity: O(1)
        :param value: the value to added
        :return: nothing
        """
        position = self.find(value)
        if position is not None:
            if self.get_size()-1 == position:
                self.table.pop()
            else:
                self.swap(position, len(self.table)-1)
                self.table.pop()
                parent = self.parent(position)
                if position == 0 or self.table[parent] < self.table[position]:
                    self.percolate_down(position)
                else:
                    self.percolate_up(position)


    def pop_min(self):
        """
        Removes the min node in the heap
        Returns the value it removed, or None
        Time complexity: O(log(n))*
        Space complexity: O(1)
        :return: removed value
        """
        if self.get_size() == 0:
            return None
        elif self.get_size() == 1:
            item = self.table.pop()
            return item
        else:
            self.swap(0, len(self.table)-1)
            item = self.table.pop()
            self.percolate_down(0)
            return item

    def swap(self, p1, p2):
        """
        Swaps the elements at indices p1 and p2
        Time complexity: O(1)
        Space complexity: O(1)
        :param p1: first index position
        :param p2: second index position
        :return: nothing
        """
        self.table[p1], self.table[p2] = self.table[p2], self.table[p1]

    def percolate_up(self, position):
        """
        Moves node at index position up the tree until it is in the proper place
        Time complexity: O(log(n))*
        Space complexity: O(1)
        :param position: index position
        :return: nothing
        """
        parent = self.parent(position)
        if position > 0 and self.table[position] < self.table[parent]:
            self.swap(position, parent)
            self.percolate_up(parent)

    def percolate_down(self, position):
        """
        Moves node at index position down the tree until it is in the proper place
        Time complexity: O(log(n))*
        Space complexity: O(1)
        :param position: index position
        :return: nothing
        """
        if self.has_left(position):
            left = self.left_child(position)
            small_child = left
            if self.has_right(position):
                right = self.right_child(position)
                if self.table[right] < self.table[left]:
                    small_child = right
            if self.table[small_child] < self.table[position]:
                self.swap(position, small_child)
                self.percolate_down(small_child)  # recur at position of small child

def heap_sort(unsorted):
    """
    Given an unsorted list, performs Heap Sort
    Returns the sorted list
    Time complexity: O(n^2)
    Space complexity: O(n)
    :param unsorted: unsorted list
    :return: sorted list
    """
    heap = BinaryMinHeap()
    n = len(unsorted)
    sort = [0] * n
    for i in unsorted:
        heap.heap_push(i)
    for i in range(n):
        min = heap.pop_min()
        sort[i] = min
    return sort
