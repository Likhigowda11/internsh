import pandas as pd

marks = pd.Series([78, 85, 60, 88, 90], index=['A', 'B', 'C', 'D', 'E'])
print(marks)

# apply condition
mask = marks >= 80
print(mask)

# filter using mask
# filter using mask
filtered_marks = marks[mask]
print(filtered_marks)

filtered_marks = marks[marks >= 80]
print(filtered_marks)

