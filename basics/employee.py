import json
filepath = "employee.json"

def loadEmployees():
    with open(filepath, "r") as file:
        empData = json.load(file)
    return empData

def saveEmployees():
    empData = loadEmployees()
    with open("updEmployee.json", "w") as file:
        file.write(json.dumps(empData, indent=2))


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
    empData = loadEmployees()
    inp = int(input("\nEnter employee you want to update: "))
    
    for x in empData:
        if inp == x["id"]:
            print(f"Employee found!")
            while True: 
                inp = int(input("\n0. Exit \n1. Update Employee Name \n2. Update Employee Role \n3. Update Employee Salary \n\nEnter Operation: "))
                
                if inp == 0:
                    break
                elif inp == 1:
                    name = input(f"Enter new name for Employee {x["id"]}: ")
                    x["name"] = name
                elif inp == 2:
                    role = input(f"Enter new role for Employee {x["id"]}: ")
                    x["role"] = role
                elif inp == 3:
                    salary = input(f"Enter new salary for Employee {x["id"]}: ")
                    x["salary"] = salary
                else:
                    continue

                with open (filepath, "w") as file:
                    file.write(json.dumps(empData, indent=2))     
                
                return
    print(f"Employee not found!")

def addEmployee():
    
    
    
    






while True:
    x = int(input("\n0. Exit \n1. Search for Employee \n2. Update Employee  \n3. Add Employee \n4. Remove Employee \n5. Print Employees \n\nEnter operation: "))

    if x == 0:
        break
    elif x == 1:
        searchEmployee()
    elif x == 2:
        updateEmployee()
    elif x == 3:
        addEmployee()
    elif x == 4:
        removeEmployee()
    elif x == 5:
        printEmployees()
        
    else:
        continue










'''
right now I have a list of objects - let's have real data of 15 json employees first
empData is list of json objects

update Employee
    - load data
    - ask the user which part he wants to modify
    - modify specific chunck
    - re-write back the updated 


'''