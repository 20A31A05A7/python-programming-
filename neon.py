l=list(map(int,input("enter the number").split()))
for i in l:
    s=i*i
    a=0
    while s>0:
        a=a+(s%10)
        s=s//10
    if a==i:
        print(i)
