
"""
Linked is a colletction of nodes where each node has it data and pointer to the hext node and 
the head points the starting node and tail points to the ending node.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    

class LinkedList:
    def __init__(self, data):
        new_node = Node(data)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next

    def append_data(self, data):   #Edge cases when list is emypy and have data
        if  self.length == 0:
            node = Node(data)
            self.head = node
            self.tail =node
        else:
            new_node = Node(data)
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1

    def pop_data(self): #Edge cases when list is empty, with only one node and with multiple node.
        if self.length == 0:
            return None
        
        else:
            pre  = self.head
            temp = self.head
            while temp.next is not None:
                pre = temp   
                temp = temp.next
            self.tail = pre 
            self.tail.next= None
            self.length -= 1

            if self.length == 0:  #Edge case: When you pop the only one remaining node
                self.head = None
                self.tail = None
            return temp
        
    def prepend_data(self,data):  # Edge cases whenlist is empty  and when list contains one or multiple nodes.
        new_node = Node(data)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            new_node.next = self.head
            self.head = new_node
            self.length += 1
        return data

    def pop_first(self):  #edge case when no node in the list and when only one nodea and when multiple node in the list 
        if self.length == 0:
            return None
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.length -= 1
            if self.length == 0:  # Edge case when yuo prepend only one node list.
                self.head = None
                self.tail = None
            return temp

    def get(self, index):
        """
        get the data in the linked list with index.
        """
        if index < 0 or index >= self.length-1:
            return False
        data = self.head
        for _ in range(index):
            data = self.head.next
        return data

    def set(self, index, value):
        """
        set the value in particular index in the linked list.
        """
        data = self.get(index)
        if data:
            data.value = value

        return data
    
    def insert(self, index, value):
        """
        Insert node anywhere in the linked list
        """
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self .prepend_data(value)
        if index == self.length:
            return self.append_data(value)
        new_node = Node(value)
        temp = self.get(index-1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        """
        remove any node with its index
        """
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            return self.pop_data(index)
        if index == self.length - 1:
            return self.pop_data(index)
        pre = self.get(index - 1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp
    
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp

        after = temp.next
        before = None
        for _ in range(self.length)
        after = temp.next
        temp.next = before
        before = temp
        temp = after 




        



linkedlist = LinkedList(1)

linkedlist.print_list()
linkedlist.append_data(8)
linkedlist.print_list()

#Pop when have more than one item 2 item in this case
print(linkedlist.pop_data())
#Pop when we have 1 item
print(linkedlist.pop_data())
#Pop when we have  item
print(linkedlist.pop_data())

#prepend data when no node
print(linkedlist.prepend_data(20))

#prepend dat when node is available

print(linkedlist.prepend_data(30))

# pop first with multiple node
print(linkedlist.pop_first())
# pop first with one node
print(linkedlist.pop_first())
# pop first with no node
print(linkedlist.pop_first())