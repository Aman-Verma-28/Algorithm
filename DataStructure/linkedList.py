class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    def append(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
            return
        lastNode=self.head
        while lastNode.next:
            lastNode=lastNode.next
        lastNode.next=newNode
    def printList(self):
        currentNode=self.head
        while currentNode:
            print(currentNode.data)
            currentNode=currentNode.next
    def prepend(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
            return
        newNode.next=self.head
        self.head=newNode
    def insert(self,data,node):
            

if __name__ == "__main__":
    l=LinkedList()
    l.append("A")
    l.append("B")
    l.append("C")
    l.append("D")
    l.printList()
    print("NOW AFTER PREPENDING")
    l.prepend("E")
    l.printList()
    l1=LinkedList()
    l1.prepend("AMAN")
    l1.printList()




    
    