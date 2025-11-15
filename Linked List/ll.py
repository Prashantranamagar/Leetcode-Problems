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

    def append_data(self, data):  # Edge cases when list is emypy and have data
        if self.length == 0:
            node = Node(data)
            self.head = node
            self.tail = node
        else:
            new_node = Node(data)
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def pop_data(
        self,
    ):  # Edge cases when list is empty, with only one node and with multiple node.
        if self.length == 0:
            return None

        else:
            pre = self.head
            temp = self.head
            while temp.next is not None:
                pre = temp
                temp = temp.next
            self.tail = pre
            self.tail.next = None
            self.length -= 1

            if self.length == 0:  # Edge case: When you pop the only one remaining node
                self.head = None
                self.tail = None
            return temp

    def prepend_data(
        self, data
    ):  # Edge cases whenlist is empty  and when list contains one or multiple nodes.
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

    def pop_first(
        self,
    ):  # edge case when no node in the list and when only one nodea and when multiple node in the list
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
        if index < 0 or index >= self.length - 1:
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
            return self.prepend_data(value)
        if index == self.length:
            return self.append_data(value)
        new_node = Node(value)
        temp = self.get(index - 1)
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
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

    # Find the middle node of the linked list
    """
    Implement the find_middle_node method for the LinkedList class.
    Note: this LinkedList implementation does not have a length member variable.
    If the linked list has an even number of nodes, return the first node of the second half of the list.
    Keep in mind the following requirements:
    The method should use a two-pointer approach, where one pointer (slow) moves one node at a time and the other pointer (fast) moves two nodes at a time.
    When the fast pointer reaches the end of the list or has no next node, the slow pointer should be at the middle node of the list.
    The method should return the middle node when the number of nodes is odd or the first node of the second half of the list if the list has an even number of nodes.
    The method should only traverse the linked list once.  In other words, you can only use one loop.
    """

    def middle_node(self):  # Two pointer approach,
        fast = self.head
        slow = self.head
        while slow.next is not None or fast.next.next is not None:
            slow = slow.next
            fast = fast.next, next
        return slow

    """
    LL has loop or not
    """

    def ll_has_loop(self):
        fast = self.head
        slow = self.head
        while slow.next is not None or fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    """"
    Removes Duplicates
    You are given a singly linked list that contains integer values, where some of these values may be duplicated.
    Note: this linked list class does NOT have a tail which will make this method easier to implement.
    Your task is to implement a method called remove_duplicates() within the LinkedList class that removes all duplicate values from the list.
    Your method should not create a new list, but rather modify the existing list in-place, preserving the relative order of the nodes.
    You can implement the remove_duplicates() method in two different ways:
    Using a Set - This approach will have a time complexity of O(n), where n is the number of nodes in the linked list. You are allowed to use 
    the provided Set data structure in your implementation.
    Without using a Set - This approach will have a time complexity of O(n^2), where n is the number of nodes in the linked list. You are not 
    allowed to use any additional data structures for this implementation.
    Input:
    LinkedList: 1 -> 2 -> 3 -> 1 -> 4 -> 2 -> 5
    Output:
    LinkedList: 1 -> 2 -> 3 -> 4 -> 5
    """

    def remove_duplicates(self):
        values = set()
        previous = None
        current = self.head
        while current:
            if current.value in values:
                previous.next = (
                    current.next
                )  # always hit else block where previous is set to surrent  .
                self.length -= 1
            else:
                values.add(current.value)
                previous = current
            current = current.next

    """
    LL Binary to decimal
    Your task is to implement the binary_to_decimal method for the LinkedList class. This method should convert a binary number, represented as a linked list, to its decimal equivalent.
    In this context, a binary number is a sequence of 0s and 1s. The LinkedList class represents this binary number such that each node in the linked list contains a single digit (0 or 1) of the binary number, and the whole number is formed by traversing the linked list from the head to the end.
    The binary_to_decimal method should start from the head of the linked list and use each node's value to calculate the corresponding decimal number. The formula to convert a binary number to decimal is as follows:
    To put it in simple terms, each digit of the binary number is multiplied by 2 raised to the power equivalent to the position of the digit, counting from right to left starting from 0, and all the results are summed together to get the decimal number.
    The binary_to_decimal method should return this calculated decimal number.
    """

    def binary_to_decimal(self):
        num = 0
        current = self.head
        while current:
            num = num * 2 + current.value
            current = current.next
        return num

    """"
    LL Reverse Between ( Interview Question)
    ⚠️ Advanced Challenge Alert: Linked List Mastery!

    Welcome to what many consider the pinnacle of Linked List challenges in this course! This exercise is not just a test of your coding skills, but also a measure of your problem-solving ability and understanding of complex data structures.
    Here's how you can tackle it:
    Visualize the Problem: Before diving into coding, grab a pen and paper. Sketch out the linked list and visualize each step of the process. This approach isn't just for beginners; it's exactly how seasoned developers plan their attack on complex problems.
    Seek Understanding Over Speed: Take your time to really grasp each part of the problem. The goal here is deep understanding, not just a quick solution. If you find yourself stuck, that's a part of the learning process.
    It's Okay to Take a Break: Feel free to step away from this challenge and return later. This course is designed to equip you with a growing set of skills, and sometimes, a bit of distance can bring new insights.
    Approach Like a Pro: Remember, facing a challenging problem is what being a professional developer is all about. Use this exercise to think, plan, and code like a pro.

    Now, let's dive into the exercise:   
    You are given a singly linked list and two integers start_index and end_index.
    Your task is to write a method reverse_between within the LinkedList class that reverses the nodes of the linked list from start_index to  end_index (inclusive using 0-based indexing) in one pass and in-place.
    Note: the Linked List does not have a tail which will make the implementation easier.
    Assumption: You can assume that start_index and end_index are not out of bounds.

    Input
    The method reverse_between takes two integer inputs start_index and end_index.
    The method will only be passed valid indexes (you do not need to test whether the indexes are out of bounds)
    Output
    The method should modify the linked list in-place by reversing the nodes from start_index to  end_index.
    If the linked list is empty or has only one node, the method should return None.
    Example
    Suppose the linked list is 1 -> 2 -> 3 -> 4 -> 5, and start_index = 2 and end_index = 4. Then, the method should modify the linked list to 1 -> 2 -> 5 -> 4 -> 3 .
    Constraints
    The algorithm should run in one pass and in-place, with a time complexity of O(n) and a space complexity of O(1).
    I highly recommend that you draw the Linked List out on a piece of paper so you can visualize the steps.
    """

    def reverse_between(self, start_index, end_index):
        if self.length <= 1:
            return

        dummy_node = Node(0)
        dummy_node.next = self.head
        previous_node = dummy_node

        for i in range(start_index):
            previous_node = previous_node.next

        current_node = previous_node.next

        for i in range(end_index - start_index):
            node_to_move = current_node.next
            current_node.next = node_to_move.next
            node_to_move.next = previous_node.next
            previous_node.next = node_to_move

        self.head = dummy_node.next

    """
    
    ⚠️ CAUTION: Advanced Challenge Ahead!
    This Linked List problem is significantly more challenging than the ones we've tackled so far. It's common for students at this stage to find this exercise demanding, 
    so don't worry if you're not ready to tackle it yet. It's perfectly okay to set it aside and revisit it later when you feel more confident.
    If you decide to take on this challenge, I strongly advise using a hands-on approach: grab a piece of paper and visually map out each step.
    This problem requires a clear understanding of how elements in a Linked List interact and move. By now, you've observed numerous Linked List
     animations in the course, which have prepared you for this moment.
    This exercise will be a true test of your ability to apply those concepts practically. Remember, patience and persistence are key here!
    Now, here is the exercise:
    Implement the partition_list member function for the LinkedList class, which partitions the list such that all nodes with values less than x come before nodes with values greater than or equal to x.
    Note:  This linked list class does NOT have a tail which will make this method easier to implement.
    The original relative order of the nodes should be preserved.

    Details:
    The function partition_list takes an integer x as a parameter and modifies the current linked list in place according to the specified criteria. If the linked list is empty (i.e., 
    head is null), the function should return immediately without making any changes.
    Example 1:
    Input:
    Linked List: 3 -> 8 -> 5 -> 10 -> 2 -> 1 x: 5
    Process:
    Values less than 5: 3, 2, 1
    Values greater than or equal to 5: 8, 5, 10
    Output:
    Linked List: 3 -> 2 -> 1 -> 8 -> 5 -> 10

    Example 2:
    Input:
    Linked List: 1 -> 4 -> 3 -> 2 -> 5 -> 2 x: 3
    Process:
    Values less than 3: 1, 2, 2
    Values greater than or equal to 3: 4, 3, 5
    Output:
    Linked List: 1 -> 2 -> 2 -> 4 -> 3 -> 5

    Tips:
    While traversing the linked list, maintain two separate chains: one for values less than x and one for values greater than or equal to x.
    Use dummy nodes to simplify the handling of the heads of these chains.
    After processing the entire list, connect the two chains to get the desired arrangement.
    Note:
    The solution must maintain the relative order of nodes. For instance, in the first example, even though 8 appears before 5 in the original list, 
    the partitioned list must still have 8 before 5 as their relative order remains unchanged.
    Note:
    You must solve the problem WITHOUT MODIFYING THE VALUES in the list's nodes (i.e., only the nodes' next pointers may be changed.)

    """

    def partition_list(self, x):
        if not self.head:
            return None

        dummy1 = Node(0)
        dummy2 = Node(0)
        prev1 = dummy1
        prev2 = dummy2
        current = self.head

        while current:
            if current.value < x:
                prev1.next = current
                prev1 = current
            else:
                prev2.next = current
                prev2 = current
            current = current.next

        prev1.next = None
        prev2.next = None
        prev1.next = dummy2.next

        self.head = dummy1.next


# LL Find Kth Node From End

"""
Implement the find_kth_from_end function, which takes the LinkedList (ll) and an integer k as input, and returns the k-th node from the end of the linked list WITHOUT USING LENGTH.
Given this LinkedList:
1 -> 2 -> 3 -> 4
If k=1 then return the first node from the end (the last node) which contains the value of 4.
If k=2 then return the second node from the end which contains the value of 3, etc.
If the index is out of bounds, the program should return None.
The find_kth_from_end function should follow these requirements:
The function should utilize two pointers, slow and fast, initialized to the head of the linked list.
The fast pointer should move k nodes ahead in the list.
If the fast pointer becomes None before moving k nodes, the function should return None, as the list is shorter than k nodes.
The slow and fast pointers should then move forward in the list at the same time until the fast pointer reaches the end of the list.
The function should return the slow pointer, which will be at the k-th position from the end of the list.

This is a separate function that is not a method within the LinkedList class. This means you need to indent the function all the way to the LEFT. 
"""


def find_kth_from_end(ll, k):
    slow = fast = ll.head
    for _ in range(k):
        if fast is None:
            return None
        fast = fast.next

    while fast:
        slow = slow.next
        fast = fast.next

    return slow


linkedlist = LinkedList(1)

linkedlist.print_list()
linkedlist.append_data(8)
linkedlist.print_list()

# Pop when have more than one item 2 item in this case
print(linkedlist.pop_data())
# Pop when we have 1 item
print(linkedlist.pop_data())
# Pop when we have  item
print(linkedlist.pop_data())

# prepend data when no node
print(linkedlist.prepend_data(20))

# prepend dat when node is available

print(linkedlist.prepend_data(30))

# pop first with multiple node
print(linkedlist.pop_first())
# pop first with one node
print(linkedlist.pop_first())
# pop first with no node
print(linkedlist.pop_first())
