print("\nAge Calculator - Know How many days you have lived!\n")

while True: 
    check = input("Do you want to calculate your Age? (0 or n to Exit) ")
    if check == "0" or "n" or "N":
        break

    name = input("Enter your Name: ")
    birthDate = int(input("Enter Birth Date: "))
    birthMonth = int(input("Enter Birth Month: "))
    birthYear = int(input("Enter Birth Year: "))

    print("\nEnter D/M/Y from which you want to calculate {name}'s Age: \n")
    fromDate = int(input("Date: "))
    fromMonth = int(input("Month: "))
    fromYear = int(input("Year: "))

    year = fromYear - birthYear

    # Month
    if birthMonth > fromMonth:
        month = (12-birthMonth) + fromMonth
        year-=1
    elif birthMonth < fromMonth:
        month = fromMonth - birthMonth
    else :
        month = 0

    # Date
    if birthDate > fromDate:
        day = (30-birthDate) + fromDate
        month-=1
    elif birthDate < fromDate:
        day = fromDate - birthDate
    else :
        day = 0

    daysLived = (365*year) + (30*month) + day

    print(f"{name} have lived {year} years, {month} months and {day} days")
    print(f"{name} have lived {daysLived} days\n")
