class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    """
    follows FIFO(first in first out) order

    """
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp.next

    def enqueue(self, value):
        """
        add node to the last of the queue
        edge case when self.legth is 0 and when length is one or more
        """
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        return True
    
    def dequeue(self):
        """
        remove node from the first of tne queue
        Edge Cases : when queue is empty, when queue has one node and when multiple node.
        """
        if self.length == 0:
            return False
        
        temp = self.first    
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length -= 1
        return temp


