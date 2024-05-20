
print("Welcome to my Computer Quiz!\n")

playing = input("Do you want to play? \n")

if playing.lower() != "yes":
    quit()
print("Okay, Let's Play! :) \n")




score = 0

print("What is full form of CPU?")
answer = input()
if answer.lower() == "central processing unit":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect!\n")


print("What is full form of GPU?")
answer = input().lower()
if answer == "graphics processing unit":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect!\n")


print("What is full form of RAM?")
answer = input()
if answer.lower() == "random access memory":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect!\n")


print("What is full form of PSU?")
answer = input()
if answer.lower() == "power supply":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect!\n")


print("What is full form of USB?")
answer = input()
if answer.lower() == "universal serial bus":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect!\n")


print("You got " + str(score) + " questions right! \n") 
"""print("You got" + score + "score!")  -- Not working because not int not str."""
#print("You got ", score, "score!")
#print(f"You got {str(score)} score! \n") #f-string doesn't need to str(), It already covert to str by {}.
print(f"Congratulations! You got {int((score/5)*100)}% \n")