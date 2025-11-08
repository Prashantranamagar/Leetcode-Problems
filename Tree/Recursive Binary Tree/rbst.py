"""
Recursive inary Search Tree
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


class BST:
    """
    Edge Cases: if root is none ,when the value is duplicate,   root is not none

    """

    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node

        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            if new_node.value > temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    # For Iterative approach
    def contains(self, value):
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False

    # For`Recursive` approach

    def __r_insert(self, current_node, value):
        if current_node == None:
            return Node(value)
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value)
        return current_node

    def r_insert(self, value):
        if self.root is None:
            self.root = Node(value)
        self.__r_insert(self.root, value)

    def __r_contains(self, current_node, value):
        if current_node == None:
            return None
        if value == current_node:
            return True
        if value < current_node:
            return self.__r_contains(current_node.left, value)
        if value > current_node:
            return self.__r_contains(current_node.right, value)

    def _r_contains(self, value):
        current_node = self.root
        return self.__r_contains(current_node, value)

    def min_value(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value

    def __delete_node(self, current_node, value):
        if current_node == None:
            return None
        if value < current_node.value:
            current_node.left = self.__delete_node(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self.__delete_node(current_node.right, value)
        else:
            if current_node.left == None and current_node.right == None:
                return None
            elif current_node.left == None:
                current_node = current_node.right
            elif current_node.right == None:
                current_node = current_node.left
            else:
                sub_tree_min = self.min_value(current_node.right)
                current_node.value = sub_tree_min
                current_node.right = self.__delete_node(
                    current_node.right, sub_tree_min
                )
        return current_node

    def _delete_node(self, value):
        self.root = self.__delete_node(self.root, value)


    """
    Interview questions
    1. Convert sorted list to balanced bst
    2. Invert binary tree.
    Input:
    node: A Node object representing the root of a binary tree. The Node class has attributes value, left, and right, 
    where value is the value stored in the node, and left and right are pointers to the node's left and right children, respectively.
    Output:
    The root node of the inverted binary tree.
    Requirements:
    The method must be recursive. It should work by traversing the tree and swapping the left and right children of every node encountered.
    If the input tree is empty (i.e., node is None), the method should return None.
    The inversion should happen in-place, meaning you should not create a new tree but instead modify the existing tree structure.
    The method should handle binary trees of any size and structure, ensuring that every node's left and right children are swapped.
    """
    def invert(self):
        self.root = self.__invert_tree(self.root)

    def __invert_tree(self, node):
        if node is None:
            return None
    
        temp = node.left
        node.left = self.__invert_tree(node.right)
        node.right = self.__invert_tree(temp)
        
        return node




my_tree = BST()
print(my_tree.root)

print(my_tree.insert(4))
print(my_tree.insert(6))
print(my_tree.insert(99))


print("BST Contains 27:")
print(my_tree.contains(27))

print("\nBST Contains 17:")
print(my_tree.contains(17))
