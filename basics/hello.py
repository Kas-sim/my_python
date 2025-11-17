def createAccount():
    username = input("Enter username: ")
    password = input("Enter Password: ")
    
    hashedPass = ""

    for x in password:
        y = ord(x)
        z = chr(y+9)
        hashedPass += z

    with open("accountData.txt", "r") as file:
        line = file.read()
        if hashedPass in line:
            return
        else:
            with open("accountData.txt", "a") as file:
                file.write(f"{username} - {hashedPass}\n")

def login():
    usernme = input("Enter username: ")
    password = input("Enter Password: ")
    hashedPass = ""

    with open("accountData.txt", "r") as file:
        line = file.read()
        if hashedPass in line:
            print("Login Successful!")



while True:
    x = input(" Enter funciton you want (-1 to quit): ")    
    if x == "0":
        createAccount()
    elif x == "1":
        login()
    elif x == "-1":
        break
    else:
        break