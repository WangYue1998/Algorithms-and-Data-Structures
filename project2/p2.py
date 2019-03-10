"""
PROJECT 2 - Recursion
Name: Yue Wang
PID: A54267282
"""

from Project2.LinkedNode import LinkedNode

def insert(value, node=None):
    """Insert the given value into the linked list that has head node
    The value should be inserted such that the list remains in ascending order
    Return the starting node of the linked list"""
    if node is None or node.value >= value:
        node = LinkedNode(value, node)
    else:
        node.next_node = insert(value, node.next_node)
    return node


def string(node):
    """Generate and return a string representation of the list,
    starting at node
    The values should be separated by a comma and a single space,
    with no leading or trailing comma"""
    
    if node is None:
        return ""
    else:
        if node.next_node is None:
            return str(node.value)
        else:
            return str(node.value) +", "+string(node.next_node)
        

    



def reversed_string(node):
    """Generate and return a string representation of the list with
    head node, in reverse order
    The values should be separated by a comma and a single space,
    with no leading or trailing comma """
    if node is None:
        return ""
    else:
        if node.next_node is None:
            return str(node.value)
        else:
            return reversed_string(node.next_node)+", "+str(node.value) 
    


def remove(value, node):
    """Remove the first node in the list with the given value starting at head node
    Return the starting node of the linked list"""
    if node is not None:
        if node.value == value:
            node = node.next_node
        else:
            node.next_node = remove(value, node.next_node)
    return node


def remove_all(value, node):
    """Remove all nodes in the list with the given value starting at head node
    Return the starting node of the linked list"""
    if node is not None:
        if node.value == value:
            node = remove_all(value, node.next_node)
        else:
            node.next_node = remove_all(value, node.next_node)
    return node

def search(value, node):
    """Looks for value in list starting with head node
    Returns True if the value is in the list and False if it is not in the list"""
    if node is None:
        return 0
    else:
        if node.value == value:
            return 1
        else:
            return search(value, node.next_node)


def length(node):
    """Calculates and returns the length of the list starting with head node"""
    if node is None:
        return 0
    else:
        return 1 + length(node.next_node)


def sum_all(node):
    """Calculates and returns the sum of the list starting with head node"""
    if node is None:
        return 0
    else:
        return node.value + sum_all(node.next_node)


def count(value, node):
    """Counts how many times the given value occurs in the list starting at head node"""
    if node is None:
        return 0
    else:
        if node.value == value:
            return 1 + count(value, node.next_node)
        else:
            return count(value, node.next_node)
