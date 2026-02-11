import pandas as pd
grades = pd.Series([85, None, 92, 45, None, 78, 55])
print(grades)

print(grades.isnull())

print(grades.fillna(0))

mask = grades >= 60
print(mask)