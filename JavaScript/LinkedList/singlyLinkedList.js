class Node{
    constructor(value){
        this.value = value
        this.next=null
    }
}

class LinkedList{
    constructor(){
        this.head= null
        this.tail = null
        this.length = 0
    }

    //push adding node ata the end of list
    push(value){
        const node = new Node(value)
        if(!this.head){
            this.head = node
            this.tail = this.head
        }
        this.tail.next = node
        this.tail = node
        this.length ++
        return this
    }
    //pop  removing the last node
    pop(){
        if (!this.head){ return undefined}
        let current =this.head
        let newtail = current
        while(current.next){
            newtail = current
            current= current.next
        }
        this.tail = newtail
        this.tail.next = null
        this.length --
        return current  //return  the value of the node removed
    }

    //add node at the beginning of list
    unshift(value){
        const node = new Node(value)
        if (!this.head){
            this.head = node 
            this.tail = this.head
        }else{
            node.next = this.head    //heare this.head points to the old node in the list
            this.head = node
            this.length ++
            return this
            
            

        }
    }
    
    //shift  rmove node at the begonnong
    shift(){
        if (!this.head){
            return undefined
        }
         var current = this.head
        this.head = current.next
        this.length --
        if(this.length === 0){
            this.tail =null
        }
        return current  //return value of the node removed

    }

    // get the node at the given index
    get(index){
        if(index<0 || index>=0){
            return
        }
        var counter = 0
        var current = this.head
        while(index !== counter){
            current = current.next
            counter ++
        }
        return current
    }

    // set the node at the given index
    set(index, value){
        var foundNode = this.get(index)
        if(foundNode){
            foundNode.value = value
            return true
        }
        return false
    }

    //insert at anywhere in the list

    insert(index, value){
        if(index<0 || index>=this.length){
            return false
        }
        if(index === 0){
            this.unshift(value)
            return true
        }
        if(index === this.length-1){
            this.push(value)
            return true
        }
        let newNode = new Node(value)
        let previous = this.get(index-1)
        let temp = previous.next
        previous.next = newNode
        newNode.next = temp
        this.length ++
        return true
    } 
    
    //remove at anywhere in the list

    remove(index, value){
        if (index<0 || index>=this.length){
            return false
        }
        if (index === 0){
            this.shift()
            return true
        }
        if (index === this.length-1){
            this.pop()
            return true
        }
        let previousNode = this.get(index-1)
        let removed =previousNode.next
        previousNode.next = removed.next
        this.length --
        return removed

    }

    //REVERSE LINKEDLIST
    reverse(){
        var node = this.head
        this.head = this.tail 
        this.tail = node
        var next;
        var prev = null;
        for(i=0; i<this.length; i++){
            next =node.next
            node.next=prev
            prev = node
            node =next
        }
        return this
    }
}