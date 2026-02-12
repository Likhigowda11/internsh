import pandas as pd

df = pd.read_csv(r"C:\Users\likhi\OneDrive\Desktop\internship\day10\customer_orders.csv")


print("Shape before cleaning:", df.shape)

print("\nMissing values report:")
print(df.isna().sum())


numeric_cols = df.select_dtypes(include=['number']).columns

df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())

categorical_cols = df.select_dtypes(include=['object']).columns

for col in categorical_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

df.drop_duplicates(inplace=True)

print("\nShape after cleaning:", df.shape)

print("\nCleaned Data:")
print(df)
