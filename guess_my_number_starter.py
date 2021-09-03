"""
File: guessmynumber.py
----------------------
This program checks if a user's guess of a number matches that guessed by the computer
"""

import random
# use code below  to generate a random integer between 30 and 50 for example
# print(random.randint(30, 50))

# ********************************** YOUR CODE GOES BELOW HERE *********************************************************
secret_number= random.randint(1, 99) #Assigning a random number to the secret-number variable

count= 0

user = int(input("Guess my number: ")) #Allowing the user to take a guess

while user != secret_number: #creating conditions for when the user guesses right
    if user < secret_number: #creating condition for when user guesses above the secret_number
        print("value is too low, try again")
        user= int(input("Guess my number: "))
        count +=  1
    elif user > secret_number:
        print("value is too high, try again") #allowing user to try again after getting it wrong
        user= int(input("Guess my number: "))
        count +=  1

print("Congratulations You got the guess right!") #Congratulating the user for getting the answer right


