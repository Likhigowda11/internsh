import pandas as pd

data = {
    "Location": [" New York", "new york", "NEW YORK ", "Los Angeles", " los angeles "]
}

df = pd.DataFrame(data)

print("Initial Data:\n", df)
print("\nUnique Locations before fix:\n", df['Location'].unique())

df['Location'] = df['Location'].str.strip()

df['Location'] = df['Location'].str.title()

print("\nData after normalization:\n", df)
print("\nUnique Locations after fix:\n", df['Location'].unique())