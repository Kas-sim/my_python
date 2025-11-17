'''name = input("Enter your name: ")
charName = list(name)

hashed = "" 

for x in charName:
    y = ord(x)
    z = chr(y+3)
#    print(f"{x} -> {y} -> {z}")
    hashed = hashed + "".join(z)

print(f"Original name: {name} - Hashed name: {hashed}")
'''
'''
while True:
    
    name = input("Enter your name - (0 to quit): ")
    if name == "0":
        break

    hashed = "" 

    for x in name:
        y = ord(x)
        z = chr(y+3)
        hashed +=z

    print(f"Original name: {name} - Hashed name: {hashed}")

    full = (f"{name} -> {hashed}\n")
    print(full)

    with open("myFile.txt", "r") as file:
        line = file.read()

        if name in line:
            print(f"{name} is already hashed!")
            break
        else:
            with open("myFile.txt", "a") as file:
                file.write(f"{name} -> {hashed}\n")

    print("Writen in myFile.txt successfully!")
'''

'''
1. create account
    password already exist!
2. login account
3. quit applicaiton
store only hash
'''

