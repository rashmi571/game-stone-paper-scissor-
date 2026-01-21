import pandas as pd
df=pd.read_json("output.json")#for rows

print("Diaplay 2 row of first")
print(df.head(2))#by default return 5 rows start

print("Display 2 row at the last")
print(df.tail(2))#by default return 5 rows end