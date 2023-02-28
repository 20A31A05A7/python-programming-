import random
print('range 1 to 100')
n=random.randint(1,100)
guess=int(input('enter any number:'))
while n!=guess:
    if guess < n:
        print("Too Low")
        guess=int(input("Enter Number Again"))
    elif guess>n:
         print("Too High")
         guess=int(input("Enter Number Again"))
    else:
        break
print("you guessed It Right")    
