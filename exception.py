'''a=10
b=0
try:
    print(a/b)
except Exception as e:
    print('please note number',e)
print("bye")    

a=10
b=0
try:
    print(a/b)
except:
    print('please note number',Exception)
    print("bye")    
finally:
    print("dgsfhg")
print("\n")
a=10
b=0
try:
    print(a/b)
    print(a)
except Exception as e:
    print('please note number',e)
#print("bye")   invalid syntax 
finally:
    print("dgsfhg")



a=10
try:
    b=int(input("enter the number:"))
    print("resource Open")
    print(a/b)
except ZeroDivisionError as e:
    print('zero',e)
except ValueError as e:
    print('value',e)
except Exception as e:
    print("Other Error",e)
finally:
    print("end of program")


x=101
if x%2!=0:
    raise Exception("x should be even")
 
else:
    print("x is even number")
'''
x=101
if x%2!=0:
    raise Exception("x should be even")
    print('dfda')
else:
   print("x is even number")
