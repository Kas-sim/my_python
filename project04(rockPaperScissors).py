
#Rock beat Scissor, Scissor beat Paper, Paper beats Rock
#Rock beats Scissor beats Paper beats Rock

#user input
#computer generate input
#comparison -> winner -> Tie

import random
#r, p, s = "Rock", "Paper", "Scissor"
#computer = random.choice([r, p, s])

moves = ["Rock", "Paper", "Scissor"]
computer = random.choice(moves)
user_input = (input("Choose between Rock Paper Scissor \n")).capitalize()
print(computer)

if user_input not in moves:
    quit("Try Again \n")

if user_input == "Rock" and computer == "Scissor":
    print("You Won!")
elif user_input == "Paper" and computer == "Rock":
    print("You Won!")
elif user_input == "Scissor" and computer == "Paper":
    print("You Won!")
elif user_input == computer:
    print("Tie")
else:
    print("Computer Won!")