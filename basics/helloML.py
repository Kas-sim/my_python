import pandas as pd

df = pd.read_json('TestEmployee.json')
# print(df)

# print(df.head())
# print(f"\n{df.tail()}")
# print(df.info())

# print(f"{df[['name', 'salary']]}")

# print(df.loc[6])
# print(df.describe())

sorted_salary = df['salary'].sort_values(ascending=False)
# print(sorted_salary)

print(f"\nAt our company, Average Salary is: { sorted_salary.mean() }")
print(f"\nAt our company, Highhest Salary is: { sorted_salary.iloc[0] } ")
print(f"\nAt our company, Minimum Salary is: { sorted_salary.iloc[-1]} ")

# print( df.iloc[16] )

# print( df.loc[0:8, ['name', 'salary']])

# print(df[df['salary'] > 220000])

# print(df[ (df['salary'] > 100000) & (df['name'] != 'qasim') ])