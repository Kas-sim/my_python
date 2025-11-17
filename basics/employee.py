import json
filepath = "employee.json"

def loadEmployees():
    with open(filepath, "r") as f:
        empData = json.load(f)
    return empData

def printEmployees():
    empData = loadEmployees()
    print("\n")
    for x in empData:
        print(f"{x["id"]}. {x["name"]} -> {x["role"]}")
    print("\n")

def searchEmployee():
    empData = loadEmployees()
    inp = int(input("\nEnter Employee id: "))
    for x in empData:
        if x["id"] == inp:
            print("Employee found!")
            print(f"{x["name"]} has empolyee id {x["id"]}\n") 
            return
    print(f"Employee with {inp} not found!")

def updateEmployee():



while True:
    x = int(input("\n0. Exit \n1. Search for Employee \n2. Add Employee \n3. Update Employee \n4. Print Employees \n\nEnter operation: "))

    if x == 0:
        break
    elif x == 1:
        searchEmployee()
    elif x == 2:
        updateEmployee()
    elif x == 3:
        addEmployee()
    elif x == 4:
        printEmployees()
    else:
        continue










'''
right now I have a list of objects - let's have real data of 15 json employees first
empData is list of json objects

update Employee
    - load data
    - modify specific chunck
    - re-write into 

'''