"""
# Project 6
# Name: Yue Wang
# PID: A54267282
"""
class Node:
    # DO NOT MODIFY THIS CLASS #
    __slots__ = 'value', 'parent', 'left', 'right'

    def __init__(self, value, parent=None, left=None, right=None):
        """
        Initialization of a node
        :param value: value stored at the node
        :param parent: the parent node
        :param left: the left child node
        :param right: the right child node
        """
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right

    def __eq__(self, other):
        """
        Determine if the two nodes are equal
        :param other: the node being compared to
        :return: true if the nodes are equal, false otherwise
        """
        if type(self) is not type(other):
            return False
        return self.value == other.value

    def __str__(self):
        """String representation of a node by its value"""
        return str(self.value)

    def __repr__(self):
        """String representation of a node by its value"""
        return str(self.value)


class BinarySearchTree:

    def __init__(self):
        # DO NOT MODIFY THIS FUNCTION #
        """
        Initializes an empty Binary Search Tree
        """
        self.root = None
        self.size = 0

    def __eq__(self, other):
        """
        Describe equality comparison for BSTs ('==')
        :param other: BST being compared to
        :return: True if equal, False if not equal
        """
        if self.size != other.size:
            return False
        if self.root != other.root:
            return False
        if self.root is None or other.root is None:
            return True  # Both must be None

        if self.root.left is not None and other.root.left is not None:
            r1 = self._compare(self.root.left, other.root.left)
        else:
            r1 = (self.root.left == other.root.left)
        if self.root.right is not None and other.root.right is not None:
            r2 = self._compare(self.root.right, other.root.right)
        else:
            r2 = (self.root.right == other.root.right)

        result = r1 and r2
        return result

    def _compare(self, t1, t2):
        """
        Recursively compares two trees, used in __eq__.
        :param t1: root node of first tree
        :param t2: root node of second tree
        :return: True if equal, False if nott
        """
        if t1 is None or t2 is None:
            return t1 == t2
        if t1 != t2:
            return False
        result = self._compare(t1.left, t2.left) and self._compare(t1.right, t2.right)
        return result

    ### Implement/Modify the functions below ###

    def insert(self, value):
        """
        Takes in a value to be added to the tree as a node
        Adds the node to the tree
        Do nothing if the value is already in the tree
        O(height) time complexity
        :param value: the value to be added
        :return: no return
        """
        # Check if the tree is empty
        if self.root is None:
            self.root = Node(value, None)
            self.size += 1
            return
        else:
            current_node = self.root
            while current_node is not None:
                if value == current_node.value:
                    return
                if value < current_node.value:
                    # If there is no left child, add the new
                    # node here; otherwise repeat from the
                    # left child.
                    if current_node.left is None:
                        current_node.left = Node(value, current_node)
                        self.size += 1
                        current_node = None
                    else:
                        current_node = current_node.left
                else:
                    # If there is no right child, add the new
                    # node here; otherwise repeat from the
                    # right child.
                    if current_node.right is None:
                        current_node.right = Node(value, current_node)
                        self.size += 1
                        current_node = None
                    else:
                        current_node = current_node.right

    def remove(self, value):
        """
        Takes in a key to remove from the tree
        Do nothing if the key is not found
        When removing a node with two children, replace with the minimum of the right subtree
        O(height) time complexity
        :param value: the value to remove
        :return: no return
        """
        cur = self.search(value, self.root)
        if cur is None:
            return
        if cur.value == value:
            if cur.left is None and cur.right is None:  # Remove leaf
                if cur.parent is None:  # Node is root
                    self.root = None
                elif cur.parent.left == cur:
                    cur.parent.left = None
                else:
                    cur.parent.right = None
                self.size -= 1
                return
            elif cur.left is not None and cur.right is None:  # Remove node with only left child
                if cur.parent is None:  # Node is root
                    self.root = None
                elif cur.parent.left == cur:
                    cur.parent.left = cur.left
                    cur.left.parent = cur.parent
                else:
                    cur.parent.right = cur.left
                    cur.left.parent = cur.parent
                self.size -= 1
                return
            elif cur.right is not None and cur.left is None:  # Remove node with only right child
                if cur.parent is None:  # Node is root
                    self.root = None
                elif cur.parent.left == cur:
                    cur.parent.left = cur.right
                    cur.right.parent = cur.parent
                else:
                    cur.parent.right = cur.right
                    cur.right.parent = cur.parent
                self.size -= 1
                return
            else:
                # Remove node with two children
                # Find successor (leftmost child of right subtree)
                suc = self.min(cur.right)
                cur.value = suc.value
                if suc.left is None and suc.right is None:
                    if suc.parent.left == suc:
                        suc.parent.left = None
                    else:
                        suc.parent.right = None
                else:
                    if suc.parent.left == suc:
                        suc.parent.left = suc.right
                        suc.right.parent = suc.parent
                    else:
                        suc.parent.right = suc.right
                        suc.right.parent = suc.parent
                self.size -= 1
                return  
        else:
            return
        
    def search(self, value, node):
        """
        Takes in a value to search for and a node which is the root of a given tree or subtree
        Returns the node with the given key if found, else returns the potential parent node
        Must be recursive
        O(height) time complexity
        :param value: the value to search ofr
        :param node: root of given tree
        :return: the node found or the potential parent node
        """
        if node is not None:
            if value == node.value:
                return node
            elif value < node.value:
                if node.left is None:
                    return node
                return self.search(value, node.left)
            else:
                if node.right is None:
                    return node
                return self.search(value, node.right)
        return None


    def inorder(self, node):
        """
        Returns a generator object of the tree traversed using the
            inorder method of traversal starting at the given node
        Points will be deducted if the return of this function is not 
        a generator object(hint: yield)
        Must be recursive
        O(n) time complexity
        :param node: given node
        :return: a generator object of the tree using inorder methood
        """
        if node:
            yield from self.inorder(node.left)
            yield node.value
            yield from self.inorder(node.right)
   

    def preorder(self, node):
        """
        Same as inorder, only using the preorder method of traversal
        O(n) time complexity
        :param node: given node
        :return: a generator object of the tree using preorder methood
        """
        if node:
            yield node.value
            yield from self.preorder(node.left)
            yield from self.preorder(node.right)
 

    def postorder(self, node):
        """
        Same as inorder, only using the postorder method of traversal
        O(n) time complexity
        :param node:given node
        :return:  a generator object of the tree using postorder methood
        """
        if node:
            yield from self.postorder(node.left)
            yield from self.postorder(node.right)
            yield node.value

    def depth(self, value):
        """
        Returns the depth of the node with the given value
        O(height) time complexity
        :param value: the value of node
        :return: the depth
        """
        if self.size == 0:#empty tree
            return -1
        node = self.root
        depth = 0
        while node is not None:
            if value == node.value:
                return depth
            elif value < node.value:
                node = node.left
                depth += 1
            else:
                node = node.right
                depth += 1
        return depth

    def height(self, node):
        """
        Returns the height of the tree rooted at the given node
        Must be recursive
        O(n) time complexity
        :return:  height of tree
        """
        if node is None:
            return -1
        leftheight = self.height(node.left)
        rightheight = self.height(node.right)
        return 1 + max(leftheight, rightheight)

    def min(self, node):
        """
        Returns the node with the minimum of the tree rooted at the given node
        Must be recursive
        O(height) time complexity
        :param node: given node as the root node
        :return: the minimum node
        """
        if node is None:
            return
        if node.left:
            return self.min(node.left)  # keep walking left
        else:
            return node

    def max(self, node):
        """
        Returns the node with the maximum of the tree rooted at the given node
        Must be recursive
        O(height) time complexity
        :param node: given node as the root node
        :return: the maximum node
        """
        if node is None:
            return
        if node.right:
            return self.max(node.right) # keep walking right
        else:
            return node

    def get_size(self):
        """
        Returns the number of nodes in the BST
        O(1) time complexity
        :return: the number of nodes
        """
        return self.size

    def is_perfect(self, node):
        """
        Returns a Boolean of whether or not the BST rooted at the given node is perfect
        O(n) time complexity
        :param node: rooted at the given node
        :return: Boolean
        """
        if node is None:
            return True
        if node.left is not None and node.right is None:
            return False
        if node.left is None and node.right is not None:
            return False
        result1 = self.is_perfect(node.left)
        result2 = self.is_perfect(node.right)
        return result1 and result2
   

    def is_degenerate(self):
        """
        Returns a Boolean of whether or not the BST is degenerate
        O(n) time complexity
        :return: Boolean
        """
        if self.root is None:
            return False
        if self.size == self.height(self.root) + 1:
            return True
        else:
            return False
 
