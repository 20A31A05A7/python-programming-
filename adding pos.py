class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlelinkedlist:
    def __init__(self):
        self.head=None
    def position(self,data,pos):
        nn=Node(data)
        temp=self.head
        for i in range(pos-2):
            temp=temp.next
        nn.next=temp.next
        temp.next=nn
            
    def display(self):
        if self.head==None:
            print("\nlist is empty")
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
pos=int(input("\nenter number:"))
obj.position(4,pos)       
obj.display()
pos=int(input("\nenter number:"))
obj.position(40,pos) 
obj.display()
