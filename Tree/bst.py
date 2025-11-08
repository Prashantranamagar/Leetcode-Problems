"""
# Binary tree --> where node have no more than 2 child node

Binary Search Tree --> Binary Servh Tree which have left child smaller than the parent node and right child greater than the parent node.
no duplicates allwed.

Birnary Search Tree Implementation
Create a class node initialize value, left pointer and right pointer.
create class BST
Initialize root to none

Insert node in BST
create new node
if self.root is none then
set root = new_node
set pointer temp = root
run while loop while True
if temp.value = new_node return false
if temp.value > newnode.value
    if temp.left is none
        temp.left = newnode
        return True
    temp = temp.left
if temp.value < newnode.value
    if temp.right is none
        temp.reght = newnode
        return True
    temp = temp.right

to check it contains the given value in the tree
do it simillarly concept as above.
    


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

    def contains(self, value):
        temp = self.root
        while (temp is not None):
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False


my_tree = BST()
print(my_tree.root)

print(my_tree.insert(4))
print(my_tree.insert(6))
print(my_tree.insert(99))


print('BST Contains 27:')
print(my_tree.contains(27))

print('\nBST Contains 17:')
print(my_tree.contains(17))



