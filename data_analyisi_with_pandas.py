import pandas as pd
data={
    "name":["rashmi","amna","sital","ankit","karishna"],
    "age":[21,22,23,24,None],
    "salary":[None,12000,24000,None,15000]
}
df =pd.DataFrame(data)
print("original dataframe")
print(df)

df.to_csv("output.csv",index=False)#save in csv
df.to_excel("output.xlsx",index=False)#save in excel
df.to_json("output.json",index=False)#save in json