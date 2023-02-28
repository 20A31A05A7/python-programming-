#without arg without reeturn value
'''
def multi():
    n1=int(input())
    n2=int(input())
    prod=n1*n2
    print(prod)
multi()
'''

#withiut arg with return value
'''
def multi():
    n1=int(input())
    n2=int(input())
    prod=n1*n2
    return (prod)
a=multi()
print(a)
print(multi())
'''
#with ardg withuot return value
#1 -Static Input
'''
def multi(n1,n2,n3):
    prod=n1*n2*n3
    print(prod)
multi(3,4,5)
'''

#2-Dynamic Input
'''
def multi(a,b,c):
     print(a*b*c)
n1=int(input("Enter number1 :"))
n2=int(input("Enter number2 :"))
n3=int(input("Enter number3 :"))
multi(n1,n2,n3)
'''
#3-Dynamic Input
'''
def multi(a,b,c):
     print(a*b*c)
for i in range(3):
    n1,n2,n3=map(int,input("enter number:").split())
    multi(n1,n2,n3)
'''
#with arg with return
def multi(a,b,c):
     return(a*b*c)
n1=int(input("Enter number1 :"))
n2=int(input("Enter number2 :"))
n3=int(input("Enter number3 :"))
print(multi(n1,n2,n3))

