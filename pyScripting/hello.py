"""

print("Hello Python Scripting")
print("Welcome using Arch and Neo and Git and Script - lol ;) ")


name = input("Enter name: ")
age = int(input("Enter your age: "))
print("Assalam-u-Alaikum ", name, "You are", age, ", right? ")

if age < 18:
    print(name, ",you are minor! ")
elif age >=40:
    print(name, ",you are adult! ")
else:
    print(name, ",you are human! ")


for i in range(10): 
    print(i)

print("\n")

count = 0
while count <= 10: 
    print(count)
    count+=1
"""

def greet():
    name = input("Enter name: ")
    age = int(input("Enter your age: "))


    if age < 18:
        print(name, ",you are minor! ")
    elif age >=40:
        print(name, ",you are adult! ")
    else:
        print(name, ",you are human! ")

    print("Your name - your age times\n")
    for i in range(age):
        print(name,"\n")


greet()