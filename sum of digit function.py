n=int(input('enter the number:'))
def sum_of_digits(a):
         s=0
         while(a>0):
             s+=(a%10)
             a=a//10
         return s
print(sum_of_digits(n))

