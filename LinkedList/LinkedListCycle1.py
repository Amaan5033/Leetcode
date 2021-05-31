# Definition for singly-linked list.
class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def __iter__(self):
        node=self.head
        while node:
            yield node
            node = node.next

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        val=Node(val)
        if self.head==None:
            self.head=val
            self.tail=val
        else:
           val.next=self.head
           self.head=val
    
    def updateTail(self,pos):
        tempNode=self.head
        location=0
        if pos==-1:
            return 
        if pos==0:
            self.tail.next=self.head
            return 
        while location<pos-1:
            tempNode=tempNode.next
            location+=1
        self.tail.next=tempNode.next



class Solution:
    def hasCycle(self, head):
        if head==None:
            return False
        pointer1=head
        pointer2=head.next            
        while pointer1 and pointer2:
            if pointer1.next==None or pointer2.next==None:
                    return False
            if pointer1==pointer2:
                return True
            else:
                pointer1=pointer1.next
                pointer2=pointer2.next.next
        return False


myLL=LinkedList()
myLL.addAtHead(1)
myLL.addAtHead(1)
myLL.addAtHead(1)
# myLL.addAtHead(3)
print([node.val for node in myLL])
myLL.updateTail(-1)

cycle=Solution()
print(cycle.hasCycle(myLL.head))

