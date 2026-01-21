#for practice
import pandas as pd
df=pd.read_excel("random_employee_data.xlsx")
print(df)

print("\n Information of the data")
print(df.info())

#describe deeply
deeply=df.describe()
print("\n deeply information of the data set")
print(deeply)

#find first and last rows
first_row=df.head(5)
last_row=df.tail(5)
print("\n first rows of dataframe")
print(first_row)
print("\n last rows of dataframe")
print(last_row)

#condition in column
column=df[["Name","Salary"]]
print("\n name and salary  column of the data set")
print(column)

#condition of the rows
find_poor_perfomance=df[df['Performance'] == 'Poor' ]
print("\n poor perfomance of the employee")
print(find_poor_perfomance)

#add new column bonus
df['Bonus']=df['Salary'] * 0.1
print("\n",df)

#add column using insert
df.insert(0,"Employee Id",[1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11, 12, 13, 14, 15, 16, 17, 18, 19, 20,21, 22, 23, 24, 25, 26, 27, 28, 29, 30,31, 32, 33, 34, 35, 36, 37, 38, 39, 40,41, 42, 43, 44, 45, 46, 47, 48, 49, 50])
print(df)

#Access and modify
df.loc[2,'salary']=35000
print("\n",df)
