'''
q1=""" How many months do we have in a year?
a.6 month
b.4 month
c.10month
d.12month"""
q2="""How many colors are there in a rainbow?
a.6
b.7
c.8
d.5"""
q3="""What is the capital of India?
a.Delhi
b.Mumbai
c.Hyderabad
d.Goa"""
q4=""" Name the first Prime Minister of India?
a.modhi
b.gandhi
c.nehru
d.chandrabose"""
questions={q1:"d",q2:"b",q3:"a",q4:"c"}
name=input("enter your name")
print("hello",name,"welcome to the quiz")
score=0
for i in questions:
    print(i)
    flag=input("do you want to skip the question(yes/no)")
    if flag=="yes":
        continue
    ans=input("enter the answer")
    if ans==questions[i]:
        print("your answer is correct")
        score=score+1
        print("your score is ",score)
    else:
        print("your answer is wrong and u lost 1 mark")
        score=score-1
        print("your score is ",score)
    flag2=input("do you want to quit the game(yes/no)")
    if flag2=="yes":
        break

print("your score is ",score)
    
'''
q1=""" How many months do we have in a year?
a.6 month
b.4 month
c.10month
d.12month"""
q2="""How many colors are there in a rainbow?
a.6
b.7
c.8
d.5"""
q3="""What is the capital of India?
a.Delhi
b.Mumbai
c.Hyderabad
d.Goa"""
q4=""" Name the first Prime Minister of India?
a.modhi
b.gandhi
c.nehru
d.chandrabose"""
questions={q1:"d",q2:"b",q3:"a",q4:"c"}
name=input("enter your name")
print("hello",name,"welcome to the quiz")
score=0
for i in questions:
    print(i)
    flag=input("do you want to skip the question(yes/no)")
    if flag=="yes":
        continue
    ans=input("enter the answer")
    if ans==questions[i]:
        print("your answer is correct")
        score=score+1
        print("your score is ",score)
    else:
        print("your answer is wrong and u lost 1 mark")
        score=score-1
        print("your score is ",score)
    flag2=input("do you want to quit the game(yes/no)")
    if flag2=="yes":
        break

print("your score is ",score)
                                            
