L=[1,2,3]
r=map(lambda x:x+1,L)
print(list(r))
n=2

res=map(lambda n:pow(n,2),L)
print(list(res))

name1='SAM'
(lambda name:print(name),name1)
