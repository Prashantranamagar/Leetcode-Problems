class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node 
        self.length = 1
    
    def print_list(self):
        temp = self.head
        for _ in range(self.length):
            value = temp.value
            temp = temp.next
            return value

    def append_data(self, value):
        """
        add data to the end of the list
        """
        #Edge case when no node on the list, when node on the list.
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        
        self.length += 1 
        return True
    

    def pop_data(self):
        """
        removes node from the end of the list
        """
        #Edge cases, having zero nodes, having single node, having multiple nodes.

        if self.length == 0:
            return False
        
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            tail = temp.prev
            tail.next = None
            temp.prev = None
        self.length -= 1
        return temp    
            
    def prepend(self, value):
        """
        add data from the start of the list.
        Edge cases: When list is empty, when it have data on it.
        """
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return new_node
        
    def pop_first(self):
        """
        removes the first element of the list
        Edge Cases: empty list, single node list, multiple node list.
        """
        if self.length == 0:
            return False
        
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            temp.next = None
            self.head.prev = None
        self.length -= 1
        return temp
    
    def get(self, index):
        """
        get the node of the list with its index
        same get method as singly linked list works fine but we can optimize it by 
        checking the given index greater or smaller than the mid value.
        """
        if index < 0 or index > self.length -1:
            return None
        temp = self.head
        mid = self.length //2 
        if index < mid:
            for _ in range(index):
                temp = temp.next
            return temp
        else:
            temp = self.tail 
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp
    
        

    def set(self, index, value):
        """
        set the value at particular index in the list.
        Edge cases: when the list is empty 
        """
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
        


    def insert(self, index, value):
        """
        insert node at any place in the list
        edge cases index 0 and last index
        """
        if index < 0 or index > self.length -1:
            return None
        if index == 0:
            return self.prepend(value)
        if index == self.length :
            return self.append_data(value)
        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next #or self.get(index)


        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev= new_node
        
        self.length +=1
        return True
    
    def delete(self, index):
        """
        delete node at any place in the list.
        """
        if index < 0 or index > self.length -1:
            return False

        if index == 0:
            return self.pop_first()
        
        if index == self.length - 1:
            return self.pop_data()
        
        temp = self.get(index)
        temp.next.prev = temp.prev
        temp.prev.next = temp.next

        temp.next = None
        temp.prev = None
        self.length -= 1
        return temp
    
doubly_linked_list = DoublyLinkedList(15)

print(doubly_linked_list.head.value)
print(doubly_linked_list.print_list())
