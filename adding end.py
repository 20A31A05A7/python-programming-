class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlelinkedlist:
    def __init__(self):
        self.head=None
    def insert_end(self,data):
        nb=Node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=nb
    def display(self):
        if self.head==None:
            print("list is empty")
        else:
            temp=self.head
            print(self.head.data,end='')
            temp=temp.next
            while temp:
                print('->',temp.data,end='')
                temp=temp.next
obj=singlelinkedlist()
n=Node(10)
obj.head=n
n1=Node(22)
n.next=n1
n2=Node(25)
n1.next=n2
obj.display()
print("\nAfter adding at ending")
obj.insert_end(30)
obj.display()
