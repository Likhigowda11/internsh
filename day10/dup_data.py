import pandas as pd
data= {
       "Customer_ID":[101,102,103,103],
       "Name":["alice","bob","charlie","bob"],
       "Purchase":["890","890","678","876"]
}
df = pd.DataFrame(data)
print(df)

print(df.duplicated())

print()

print(df.drop_duplicates())

print(df.drop_duplicates(keep="last"))

print(df.drop_duplicates(keep=False))

df["Joining_Date"] = pd.to_dataset(df["Joining_Date"])
print(df.types)
print(df["Joining_Date"].dt.year)
