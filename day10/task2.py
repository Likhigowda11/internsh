import pandas as pd

# Sample data
data = {
    "Price": ["$12.50", "$7.30", "$15.00", "$9.75"],
    "Date": ["2026-01-01", "2026-01-02", "2026-01-03", "2026-01-04"]
}

df = pd.DataFrame(data)

print("Initial Data Types:\n", df.dtypes)
print("\nInitial Data:\n", df)

# Correct Price conversion
df['Price'] = df['Price'].str.replace('\$', '', regex=True).astype(float)

# Convert Date
df['Date'] = pd.to_datetime(df['Date'])

print("\nData after conversion:\n", df)
print("\nData Types after conversion:\n", df.dtypes)

print("\nAverage Price:", df['Price'].mean())
print("Latest Date:", df['Date'].max())