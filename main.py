import pandas as pd

df = pd.read_csv("Data.csv")


df

df1 = pd.read_csv("Data1.csv")

df1

df2 = pd.read_csv("Data2.csv")

df2




df.tail(20)

df2.head(20)


dfconcat = pd.concat([df, df2], axis= 0)


value_counts = dfconcat["Name"].value_counts()

value_counts[value_counts > 1]

dfnoduplicate = dfconcat.drop_duplicates(subset = "Name")

dfnoduplicate[dfnoduplicate["Name"] == "Banana Fish"]


dfnoduplicate.to_csv("deita.csv")

