import pandas as pd

from sklearn.preprocessing import LabelEncoder

data = {
    "Transmission": ["Automatic", "Manual", "Automatic", "Manual", "Automatic"],
    "Color": ["Red", "Blue", "Green", "Red", "Blue"]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)
print("-" * 40)

le = LabelEncoder()
df["Transmission"] = le.fit_transform(df["Transmission"])

print("After Label Encoding (Transmission):")
print(df)
print("-" * 40)

df = pd.get_dummies(df, columns=["Color"], drop_first=True)

print("Final Encoded Dataset:")
print(df)
print("-" * 40)

print("Data Types:")
print(df.dtypes)