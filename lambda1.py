   import math
l=[]
for i in range(1,16):
    if i%2==0:
        l.append(i)
res=map(lambda x:math.sqrt(x),l)
print(list(res))


