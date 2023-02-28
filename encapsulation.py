#protected_
''''
class encap:
    _a=10
    c=12
    def encapfunction(self):
        _b=200
        print("encapfunction accessinf protected")
        print(self._a+10)
obj=encap()
print(obj._a)
obj.encapfunction()
print(obj.c)
'''
#private__
class encap:
    __a=10
    print(__a)
    def encapfunction(self):
        print("encapfaunction")
        print(self.__a)
obj=encap()
obj.encapfunction()
print(obj.__a)
