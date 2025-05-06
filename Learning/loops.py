""" My Attempt - First Loop of Python
n = int(input("Enter number of student you want ot enroll: "))
for i in range (n):
    name = input(f"Student {i+1}: " )
print(f"Total students enrolled: {n}")"""

""" (start, end, step)
for i in range (1, 11, 2):
    print(f"I Love MQ {i}")"""

""" C++ like while Loop
i = 0
while i < 5:
    print("Are you learning Python? ")
    i+=1"""

""" Basic IQ Test 
while True:
    n = int(input("Guess the number to exit the loop: "))
    if n < 0:
        break"""

""" skip - continue  
for i in range(100):
    if i % 2 == 0:
        continue 
    print(i) """

""" Even ODD Detector and List
while True:
    check = input("Play or Quit(0): ")
    if check == "0":
        break
    else: 
        n = int(input("Enter a digit: "))
        if n % 2 == 0:
            print("Heres List of Even numbers: ")
            for i in range(0, n+1, 2): 
                print(i)
        else:
            print("Heres List of Odd numbers: ")
            for i in range(1, n+1, 2):
                print(i)
                if i % 2 != 0:
                    continue
"""
