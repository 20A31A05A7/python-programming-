class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlelinkedlist:
    def __init__(self):
        self.head=None
    def inserting_beginning(self,data):
        nb=Node(data)
        nb.next=self.head
        self.head=nb
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
'''n=Node(10)
obj.head=n
n1=Node(22)
n.next=n1
n2=Node(25)
n1.next=n2'''
obj.display()
print("\nAfter adding at beginning")
obj.inserting_beginning(30)
obj.display()

            
