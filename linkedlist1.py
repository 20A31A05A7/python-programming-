class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlelinkedlist:
    def __init__(self):
        self.head=None
    def display(self):
        if self.head==None:
            print("linked list is Empty")
        else:
            temp=self.head
            print(temp.data,end='')
            temp=temp.next
            while temp:
                print("->",temp.data,end='')
                temp=temp.next
obj=singlelinkedlist()
n=Node(10)
obj.head=n
n1=Node(30)
obj.head.next=n1
n2=Node(20)
n1.next=n2
obj.display()
