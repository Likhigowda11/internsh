import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, MinMaxScaler

data = {
    "Age": [22, 25, 30, 35, 40],
    "Salary": [25000, 40000, 60000, 80000, 100000]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

scaler = StandardScaler()

standardized_data = scaler.fit_transform(df)

df_standardized = pd.DataFrame(standardized_data, columns=df.columns)

print("\nStandardized Data:")
print(df_standardized)

minmax = MinMaxScaler()

normalized_data = minmax.fit_transform(df)

df_normalized = pd.DataFrame(normalized_data, columns=df.columns)

print("\nNormalized Data:")
print(df_normalized)

plt.figure()
plt.hist(df["Salary"])
plt.title("Original Salary Distribution")
plt.show()

plt.figure()
plt.hist(df_standardized["Salary"])
plt.title("Standardized Salary Distribution")
plt.show()

plt.figure()
plt.hist(df_normalized["Salary"])
plt.title("Normalized Salary Distribution")
plt.show()