"""
File: khansole_academy.py
-------------------------
Khansole Academy is a program that teaches users how to add by asking users to input answers for the addition of two
randomly generating integers between 10 and 99 inclusive. The program returns feedback based on the User's answers.

"""

import random
# use code below  to generate a random integer between 30 and 50 for example
#print(random.randint(30, 50))

# ********************************** YOUR CODE GOES BELOW HERE *********************************************************
correct_answer = 0
while True:
    a = random.randint(10, 99) #asssigning the first number in the addition to a two digit number
    b = random.randint(10, 99) #asssigning the second number in the addition to a two digit number
    answer = a + b             #defing the variable answer as the sum of the two numbers

    print(f"What is {a} + {b}? ") #displaying the question to the user
    user_answer = int(input())    #providing room for the user's answer

    if user_answer == answer:     #relaying conditions for when user gets answer correct
        print(f"Your answer was {user_answer}")
        correct_answer += 1
        print("Your answer is correct!")
    else:
        print(f"Your answer was {user_answer}") #relaying conditions for when user gets answer wrong
        correct_answer = correct_answer - correct_answer
        print(f"Your answer is wrong 😂, the right answer is {a+b} !")
    if correct_answer == 3:
        print("Nice work! You've completed the course ✌")
        break



