class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top =new_node
        self.bottom = new_node
        self.length = 1

    def print_node(self):
        if self.length == 0:
            return None
        for _ in range(self.length):
            return self.top.value
    
    def push(self, value):
        """
        Add data from top of the stack
        Edge cases. when the stack is empty. and when there are nodes in the stack
        """
        new_node = Node(value)
        if self.top is None:
            self.top = new_node
            self.bottom = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.length += 1

    def pop(self):
        """
        take out item from the top of the stack.
        Edge cases: No item in the stack, one item in the stack, multiple item on the stack.
        """

        if self.length == 0: 
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -=1

        return temp


