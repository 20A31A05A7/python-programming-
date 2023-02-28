n=int(input())

def happynumber(n):
    if n>=10:
        s=0
        while n>0:
         r=n%10
         n=n//10
         s+=r**2
        n=s
        happynumber(n)
    else:
        if n==1:
            print('happy number')
        else:
            print('not')

happynumber(n)
