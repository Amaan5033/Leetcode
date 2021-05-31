

class Node:
  def __init__(self,val=None):
    self.val=val
    self.next=None



class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head=None
        self.tail=None
        self.length=0
        
    def __iter__(self):
        node=self.head
        while node:
            yield node
            node = node.next
       
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if self.length<=index:
          return -1
        if index==0:
          return self.head.val
        else:
          tempNode=self.head
          location=0
          while location<index-1:
                tempNode=tempNode.next
                location+=1
          return tempNode.next.val
      

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
        self.length+=1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        val=Node(val)
        if self.head==None:
          self.head=val
          self.tail=val
        else:
          self.tail.next=val
          self.tail=val
        self.length+=1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index==0:
          self.addAtHead(val)
          return
        if self.length<index:
          return
        else:
          val=Node(val)
          tempNode=self.head
          location=0
          while location<index-1:
            tempNode=tempNode.next
            location+=1
          if tempNode.next==None:
              self.addAtTail(val.val)
              return
          nextNode=tempNode.next
          val.next=nextNode
          tempNode.next=val
          self.length+=1
   
    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if self.length<=index:
          return
        if index==0:
          self.head=self.head.next
        else:
          tempNode=self.head
          location=0
          while location<index-1:
            tempNode=tempNode.next
            location+=1
          
          deleteNode=tempNode.next
          tempNode.next=deleteNode.next
          if tempNode.next==None:
            self.tail=tempNode
        self.length-=1
          


# Your MyLinkedList object will be instantiated and called as such:
myLinkedList=MyLinkedList()
myLinkedList.addAtHead(1)

myLinkedList.addAtTail(3)


myLinkedList.addAtIndex(1,2)
print([node.val for node in myLinkedList])
myLinkedList.addAtIndex(3,4) 
print([node.val for node in myLinkedList])
myLinkedList.addAtIndex(5,2)
print([node.val for node in myLinkedList])
print(myLinkedList.get(4))
print(myLinkedList.length)
myLinkedList.deleteAtIndex(4)
print([node.val for node in myLinkedList])
# myLinkedList.deleteAtIndex(1)
# print([node.val for node in myLinkedList])
# print(myLinkedList.head.val) 
# print(myLinkedList.tail.val)
# print(myLinkedList.get(0))

# print([node.val for node in myLinkedList]) 
# # myLinkedList.addAtIndex(1, 2) 
# print([node.val for node in myLinkedList])   
# # myLinkedList.get(1)              
# myLinkedList.deleteAtIndex(0)   
# print([node.val for node in myLinkedList])
# # myLinkedList.get(1)             



# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(1)
# obj.addAtTail(3)
# obj.addAtIndex(1,2)
# obj.deleteAtIndex(index)


# Input
# ["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
# [[], [1], [3], [1, 2], [1], [1], [1]]
# Output
# [null, null, null, null, 2, null, 3]

# Explanation
# MyLinkedList myLinkedList = new MyLinkedList();
# myLinkedList.addAtHead(1);
# myLinkedList.addAtTail(3);
# myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
# myLinkedList.get(1);              // return 2
# myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
# myLinkedList.get(1);              // return 3