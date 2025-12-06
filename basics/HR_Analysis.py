import pandas as pd

df = pd.read_json('TestEmployee.json')

num_of_employees = df['name'].count()
top_five_employees = df.sort_values('salary', ascending=False).head()

average_salary = df['salary'].mean()
highest_salary = df['salary'].max()
lowest_salary = df['salary'].min()
sum_salary = df['salary'].sum()


role_salary = df.groupby('role')['salary'].mean()
rounded_salary = df['salary'].round()

def salaryComparison():
    print("Enter the role you want to compare be compared & compare with \n")
    print(type(role_salary))
    role1 = input("Role 1: ").strip()
    role2 = input("Role 2: ").strip()

    if role1 not in role_salary.index:
        print(f"{role1} is not any role at our company!")
        return
    if role2 not in role_salary.index:
        print(f"{role2} is not any role at our company!")
        return

    if role_salary[role1] > role_salary[role2]:
        print(f" {role1} earns more than {role2}!")
    elif role_salary[role1] < role_salary[role2]:
        print(f" {role2} earns more than {role1}!")
    else:
        print(f" {role1} and {role2} both earns equal!")

# grouped = df.groupby('role')['salary'].agg( [ "count", "mean" ])

while True:
    x = int(input("" \
    "\n0. 0 to Exit " \
    "\n1. Number of Employees " \
    "\n2. Check Top 5 Senior Employees " \
    "\n3. Check Salaries " \
    "\n4. Compare Salaries b/w two roles " \
    "\nEnter Operation: "))
    if x == 0:
        break

    elif x == 1:
        print(num_of_employees)

    elif x == 2:
        print(top_five_employees)
        
    elif x == 3:
            print(df.describe())
            print(f"\n Yearly company gives -> { round(sum_salary) } to Employees \n")
            print(rounded_salary)
    elif x == 4:
        salaryComparison()   

    else:
        print("Invalid Operation!\n")