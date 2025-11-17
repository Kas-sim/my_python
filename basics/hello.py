def createAccount():
    username = input("Enter username: ")
    password = input("Enter Password: ")
    
    hashedPass = ""

    for x in password:
        y = ord(x)
        z = chr(y+10)
        hashedPass += z

    with open("accountData.txt", "r") as file:
        content = file.read()
        if hashedPass in content:
            print("this password already exists")
            return
        else:
            with open("accountData.txt", "a") as file:
                file.write(f"{username} - {hashedPass}\n")

def login():
    usernme = input("Enter username: ")
    password = input("Enter Password: ")

    hashedPass = ""

    for x in password:
        y = ord(x)
        z = chr(y+10)
        hashedPass += z

    with open("accountData.txt", "r") as file:
        content = file.read()
        if hashedPass in content:
            print("Login Successful!")



while True:
    x = input("Enter operatin you want to perform (0 to quit): ")    
    if x == "1":
        createAccount()
    elif x == "2":
        login()
    elif x == "0":
        break
    else:
        continue