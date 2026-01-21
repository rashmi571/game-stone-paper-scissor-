import pandas as pd
data={
    "name":["rashmi","amna","sital","ankit","karishna"],
    "age":[21,22,23,24,45],
    "salary":[600,12000,24000,15000,15000]
}
df =pd.DataFrame(data)
high_salary=df[df['salary'] > 2000]
print("employee with salary greater than 2000")
print(high_salary)

#multiple conditions
salary=df[(df['age'] > 23) & (df['salary'] > 2000)]
print("\nemployee with age greater than 2000")
print(salary)