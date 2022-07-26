/*

Linked List
collection of node each node contain some data and refrence to next node.
two special node head node and tail node.

Linked List implementation

Creating a node 

*/

class Node{
    constructor (data, next=null){
        this.data = data
        this.next = next;
    }
}

//Creating Linked List
class LinkedList{
    constructor (){
        this.head=null;
    }

    /* 
    
    Inserting node first inserting at the beginning of the linked list.
    Eg
    head => [data1, next=null]
    inserting new data
    [data2, next=head]
    [data2, next => [data1, next=null]]
    head => [data2, next => [data1, next=null]]
    
     */
    insertFirst(data){
        const node = newNode(data, this.head)
        this.head = node
        // or this can be written as this.head = newNode(data, this.head)
    }

    //get the first node of the list
    getFirst(){
        return this.head
    }

    //get last
    getLast(){
        if(!this.head){
            return null
        }
        node = this.head
        while(node){
            // if (node.next==null){
            //     return node
            // }
            if(!node.next){
                return node
            }
            node = node.next
        }
    }

    //Clear the list
    clear(){
        this.head = null
    }

    //remove first node 
    removeFirst(){
        if(!this.head){
            return
        }
        this.head = this.head.next
    }

    //Remove last node
    removeLast(){
        if(!this.head){
            return
        }
        if(!this.head.next){
            this.head = null
        }
        const previous = this.head
        const node = this.head.next
        while(node.next){
            previous =node
            node  = node.next
        }
        previous.next = null
    }

    
    //Insert Last (insert node at the end of the list)
    insertLast(data){
        const last = getLast()
        if(last){
            last.next = new Node(data)
        }else{
            this.head = new Node(data)
        }
    }


}