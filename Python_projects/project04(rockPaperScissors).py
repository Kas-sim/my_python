
#Rock beat Scissor, Scissor beat Paper, Paper beats Rock
#Rock beats Scissor beats Paper beats Rock

#user input
#computer generate input
#comparison -> winner -> Tie

import random
#r, p, s = "Rock", "Paper", "Scissor"
#computer = random.choice([r, p, s])

moves = ["Rock", "Paper", "Scissor"]
victory = 0
lost = 0
tie = 0
played = 0

while True:
    user_input = (input("Type: Rock/Paper/Scissor or Q to quit\n")).capitalize()
    computer = random.choice(moves)


    if user_input == "Q":
        print()
        print(f"You Won {victory} times!")  
        print(f"You Lost {lost} times!")
        print(f"Tie {tie} times!")
        print(f"You played {played} times!")
        quit()

    print("")
    print(computer, "\n")
    
    if user_input not in moves:
        quit("Invalid input! \n")

    if user_input == "Rock" and computer == "Scissor":
        print("You Won! \n")
        victory += 1
    elif user_input == "Paper" and computer == "Rock":
        print("You Won! \n")
        victory += 1
    elif user_input == "Scissor" and computer == "Paper":
        print("You Won! \n")
        victory += 1
    elif user_input == computer:
        print("Tie \n")
        tie += 1
    else:
        print("Computer Won! \n")
        lost += 1
    #print(f"You Won {victory} times and Lost {lost} times \n")
    
    played += 1
    