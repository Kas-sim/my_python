def hashedInput():
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    
    hashedPass = ""

    for x in password:
        y = ord(x)
        z = chr(y+10)
        hashedPass += z
    return username, hashedPass

def createAccount():
    print("\n--- Signup ---")
    username, hashedPass = hashedInput()

    with open("accountData.txt", "r") as file:
        content = file.read()
        if username in content:
            print(f"{username} is already registered!\n")
            createAccount()
        else:
            with open("accountData.txt", "a") as file:
                print(f"Congratulations, {username}\nAccount created successfully!\n")
                file.write(f"{username} - {hashedPass}\n")

def login():
    print("\n--- Login ---")
    username, hashedPass = hashedInput()

    with open("accountData.txt", "r") as file:
        content = file.read()
        if username and hashedPass in content:
            print("Login Successful!\n")
            return
        else:
            print("Login Failed!\n")
            return


while True:
    x = input("\n0. Exit \n1. Create Account \n2. Login \nEnter operation: ")    
    if x == "1":
        createAccount()
    elif x == "2":
        login()
    elif x == "0":
        break
    else:
        continue

'''
Menu with (exit, signup, login)

signup 
    create account
    only if user is not registered already!
    writing in accountData.txt

login
    check username and password exist 
    login failed or login successful
    checking from accountData.txt

'''