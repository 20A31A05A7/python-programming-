'''
class computer():
    a=10
    b=20
    print("Class Variable inside class",a)
    def config(self):
        c=100
        print("Yes")
        print("iNSTANCE access:",self.b)
lenovo=computer()
print(lenovo.a)
print(lenovo.a+lenovo.b)
dell=computer()
print("dell",dell.a)
lenovo.config()

'''
class computer():
    a=10
    b=20
    print("Class Variable inside class",a)
    def __init__(self):
        self.c=100
        print("Yes")
        print("iNSTANCE access:",self.b)
lenovo=computer()
print(lenovo.a)
print(lenovo.a+lenovo.b)
dell=computer()
print("dell",dell.a)

print(lenovo.c)

