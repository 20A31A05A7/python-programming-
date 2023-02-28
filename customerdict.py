'''import random
l=['jaya','veera','sai','santosh','ashok','kumar','raj','kumars']
d={name:random.randint(1,100) for name in l }
print(d)'''


import random
l=['jaya','veera','sai','santosh','ashok','kumar','raj','kumars']
d=dict.fromkeys(l)
for name in d:
    d[name]=random.randint(1,100)
print(d)    
