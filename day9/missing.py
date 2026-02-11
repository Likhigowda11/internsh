import pandas as pd

data = pd.Series([10,None,30,None])
print(data)

print(data.isnull())

print(data[data.isnull()])


print(data[data.notnull()])

print(data.fillna(0))

print(data.fillna(data.mean()))

print(data.dropna())