/*

Linked List Cycle II
Source:https://leetcode.com/problems/linked-list-cycle-ii/

Question:
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, 
return null.There is a cycle in a linked list if there is some node in the list that can be reached again by
continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's 
next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a 
parameter.
Do not modify the linked list.



*/


var detectCycle = function(head) {
    let fast = head
    let slow = head
    while(fast !== null && fast.next !== null){
        slow =slow.next
        fast = fast.next.next
        if (fast === slow){
            slow= head
            while (fast != slow){
                fast = fast.next
                slow =slow.next
            }
            return slow    //or u can return fast they both returns the tail where cycle start
        }
        
    }
    return null
};