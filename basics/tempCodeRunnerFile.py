






while True:
    x = int(input("\n0. Exit \n1. Search for Employee \n2. Update Employee  \n3. Add Employee \n4. Print Employees \n\nEnter operation: "))

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

