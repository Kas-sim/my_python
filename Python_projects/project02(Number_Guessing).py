#Project made on 18/5/2024

import random

Low = 1
High = 100
guesses = 0
number = random.randint(Low, High)

print("Guess the Number!\n")

while True:
    guess = int(input(f"Enter a number between ({Low}-{High}): \n"))
    guesses += 1     

    if guess < number:
        print(f"{guess} is too Low!\n")
    elif guess > number:
        print(f"{guess} is too High!\n")
    else:
        print(f"{guess} is correct!\n")
        break
print("Great Job!\n")
print(f"This round took you {guesses} guesses!\n")

#Little Modification: added \n on 19/5/2024