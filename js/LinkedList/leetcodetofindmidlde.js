var middleNode = function(head){
    let fast = slow =head
    while(fast && fast.next){
        fast = fast.next.next
        slow = slow.next

    }
    return slow
}
 //for odd numbers
// 1st iteration      2th iteration          3th iteration
// f                        f                            f
// 1->2->3->4->5      1->2->3->4->5          1->2->3->4->5    return s //3
// s                     s                         s

 //for even numbers it return the second middle node as there are two middle nodes     
// 1st iteration         2th iteration             3th iteration             4th iteration
// f                            f                               f                             f
// 1->2->3->4->5->6      1->2->3->4->5->6          1->2->3->4->5->6          1->2->3->4->5->6    return s //4
// s                        s                            s                            s
     

   

