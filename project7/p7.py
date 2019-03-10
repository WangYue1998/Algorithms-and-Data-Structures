"""
# Project 7
# Name: Yue Wang
# PID: A54267282
"""


class HashNode:
    """
    DO NOT EDIT
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __repr__(self):
        return f"HashNode({self.key}, {self.value})"


class HashTable:
    """
    Hash table class, utilizes double hashing for conflicts
    """

    def __init__(self, capacity=4):
        """
        DO NOT EDIT
        Initializes hash table
        :param tableSize: size of the hash table
        """
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity

    def __eq__(self, other):
        """
        DO NOT EDIT
        Equality operator
        :param other: other hash table we are comparing with this one
        :return: bool if equal or not
        """
        if self.capacity != other.capacity or self.size != other.size:
            return False
        for i in range(self.capacity):
            if self.table[i] != other.table[i]:
                return False
        return True

    def __repr__(self):
        pass

    def hash_function(self, x):
        """
        ---DO NOT EDIT---

        Converts a string x into a bin number for our hash table
        :param x: key to be hashed
        :return: bin number to insert hash item at in our table, -1 if x is an empty string
        """
        if not x:
            return -1
        hashed_value = 0

        for char in x:
            hashed_value = 181 * hashed_value + ord(char)

        return hashed_value % self.capacity

    def insert(self, key, value): #hidden
        """
        Inserts key(string) and value(string) into the HashTable using a HashNode
        Resolves conflicts using quadratic probing
        If a HashNode with the same key is already present, reassigns the value to the new value
        If the load factor is strictly greater than 0.75, calls grow()
        Does NOT allow insertion of empty string
        Expected time complexity O(1), Worst case O(n) time complexity
        :param key: string
        :param value: string
        :return: no return
        """
        # return the bin number of table
        index = self.hash_function(key)
        # do not insert empty string
        if index != -1:
            # insert item in empty bucket
            if self.table[index] is None:
                self.table[index] = HashNode(key, value)
                self.size += 1
            # if the key is present, update value
            elif self.table[index].key == key:
                self.table[index].value = value
            # resolve conflicts
            else:
                index = self.quadratic_probe(key)
                if self.table[index] is None:
                    self.table[index] = HashNode(key, value)
                    self.size += 1
                # if the key is present, update value
                elif self.table[index].key == key:
                    self.table[index].value = value
        # grow size
        load_factor = self.size / self.capacity
        if load_factor > 0.75:
            self.grow()

    def quadratic_probe(self, key): #hidden
        """
        Runs the quadratic hashing procedure
        bucket = (bucket + i*i) % capacity
        Returns the table index of key if key is in the table
        If key is not found in the table, returns the next available index
        :param key: string
        :return: return the table index if key in table, otherwise the next available index
        """
        # the index should be
        index = self.hash_function(key)
        # do not insert empty string
        if index != -1:
            bucketsprobed = 0
            i = 0
            while bucketsprobed < self.capacity:
                if self.table[index] is not None:
                    # if the key in the table
                    if self.table[index].key == key:
                        return index
                elif self.table[index] is None:
                    return index
                # Increment i and recompute bucket index
                i += 1
                index = (index + i * i) % self.capacity
                # Increment number of buckets probed
                bucketsprobed += 1
        return index

    def find(self, key):
        """
        Takes in a key to search for in the Hash Table
        Returns the node with the given key if found, if not found it returns False
        Expected time complexity O(1), Worst case O(n) time complexity
        :param key: the string to search for
        :return: if found, return node. Otherwise, return False
        """
        index = self.quadratic_probe(key)
        if index != -1:
            if self.table[index] is not None:
                return self.table[index]
            else:
                return False
        else:
            return False

    def lookup(self, key):
        """
        Takes in a key to search for in the Hash Table
        Returns the value of the node with the given key if found, if not found it returns False
        Expected time complexity O(1), Worst case O(n) time complexity
        :param key: the string to search for
        :return: the value of node if key is found. Otherwise, return False.
        """
        n = self.find(key)
        if n:
            return n.value
        else:
            return False

    def delete(self, key):
        """
        Takes in a key to delete in the Hash Table
        Deletes by setting node to None
        Expected time complexity O(1), O(n) time complexity
        :param key: the node (key, value) need to be None
        :return: no return
        """
        index = self.quadratic_probe(key)
        if self.table[index] is not None:
            self.table[index] = None
            self.size -= 1

    def grow(self):
        """
        Doubles capacity
        Rehashes all items in table
        O(n) time complexity
        :return: no return
        """
        self.capacity = self.capacity * 2
        self.rehash()

    def rehash(self):
        """
        A list is allowed within rehash.
        Rehashes all items inside of the table
        O(n) time complexity
        :return: no return
        """
        old = list()
        # use iteration to record existing items
        for i in range(self.capacity // 2):
            if self.table[i] is not None:
                old.append(self.table[i])
        self.table = self.capacity * [None]  # then reset table to desired capacity
        self.size = 0
        for i in old:
            index = self.quadratic_probe(i.key)
            self.table[index] = i
            self.size += 1


def string_difference(string1, string2):
    """
    A set can/must be used in string_difference and should be returned.
    Takes in two strings, uses hash tables to get the difference of characters from the strings
    Returns a set of the different characters, grouped by character
    Example: string1 = "aabbcc", string2 = "ab"
    The result would be a set containing {'a', 'b', 'cc'} - those are the differing characters between the 2 strings
    Notice how the c's grouped together in the same string object
    Uses only the HashTable class and no auxiliary containers
    Lists and Dictionaries are NOT allowed within this function
    O(n) time complexity
    :param string1: the first string need compare
    :param string2: the second string need compare
    :return: a set of difference
    """
    difference = set()
    ht = HashTable(8)
    # adding each character a key, the number of character as value
    for ch in string1:
        v = string1.count(ch)
        ht.insert(ch, v)
    # check for if string2 has same character with string1
    for c in string2:
        # return the value how many times c exists in hastable
        s = ht.lookup(c)
        # if not exist
        if s is False:
            ht.insert(c, 1)
        # if exist
        else:
            # if that c exitss in string1,value -1
            if string1.find(c) != -1:
                ht.insert(c, s - 1)
            # if only exist in string2, add value +1
            else:
                ht.insert(c, s + 1)
    # return the difference set
    for i in ht.table:
        if i is not None and i.value != 0:
            difference.add(i.key * abs(i.value))
    return difference
