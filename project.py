import random

number=random.randint(1,10)
guess=int(input("Enter Your Guess:"))

while (guess != number):
    if (guess < number):
        print("Your Guess is Higher. Try again") 
        guess=int(input("Enter Your Guess:"))
    else:
        print("Your Guess is Lower. Try Again")   
        guess=int(input("Enter Your Guess:")) 




if (guess==number):
    print("You Win!!!!!!!")

   