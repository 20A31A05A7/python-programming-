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
n=Node('w')
obj.head=n
n1=Node('i')
obj.head.next=n1
n2=Node('n')
n1.next=n2
n3=Node('n')
n2.next=n3
n4=Node('e')
n3.next=n4
n5=Node('r')
n4.next=n5
obj.display()
