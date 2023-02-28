class moverload:
    def display(self,a=None,b=None):
        print(a,b)
obj=moverload()
print("without argument")
obj.display()
print("with all argument")
obj.display(20,30)
print("wirh one argument")
obj.display(10)
print("wirh one argument")
obj.display(10)
