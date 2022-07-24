//finding the middile og=f the list


//when there is even no of nodes there are two middle nodes this function gives first middle valve 
var middleNode = function(list) {
    let fast = this.head;
    slow = this.head;
    while (fast.next && fast.next.next) {
        fast = fast.next.next;
        slow = slow.next;
    }
    return slow;
};


//when there is even no of nodes there are two middle nodes this function gives second middle valve 
var middleNode = function(list) {
    let fast = this.head;
    slow = this.head;
    while (fast && fast.next.) {
        fast = fast.next.next;
        slow = slow.next;
    }
    return slow;
};
