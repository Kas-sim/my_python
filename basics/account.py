filepath = "accountData.txt"
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

    with open(filepath, "r") as file:
        content = file.read()
        if username in content:
            print(f"{username} is already registered!\n")
            createAccount()
        else:
            with open(filepath, "a") as file:
                print(f"Congratulations, {username}\nAccount created successfully!\n")
                file.write(f"{username} - {hashedPass}\n")

def login():
    print("\n--- Login ---")
    username, hashedPass = hashedInput()

    with open(filepath, "r") as file:
        
        for line in file:
            if f"{username} - {hashedPass}" in line:
                print("Login Successful!\n")
                return
        print("Login Failed!\n")



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
    read from accountData - only if user is not registered already!
    store the hash of the password
    writing in accountData.txt

login
    checking from accountData.txt
    check if username + hashedPass exists
    login failed or login successful

'''