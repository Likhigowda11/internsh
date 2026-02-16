import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

data = {
    "SquareFootage": [800, 1200, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000],
    "Bedrooms": [2, 3, 3, 4, 4, 5, 5, 6, 6, 7],
    "Bathrooms": [1, 2, 2, 3, 3, 4, 4, 5, 5, 6],
    "Price": [150000, 200000, 250000, 300000, 350000, 450000, 500000, 600000, 650000, 2000000],  # 2000000 is an outlier
    "Location": ["Urban", "Urban", "Suburban", "Suburban", "Suburban", 
                 "Urban", "Rural", "Rural", "Urban", "Rural"]
}

df = pd.DataFrame(data)

corr_matrix = df.corr(numeric_only=True)

print("\nCorrelation Matrix:\n")
print(corr_matrix)

plt.figure(figsize=(8,6))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Matrix Heatmap")
plt.show()

print("\nHighly Correlated Feature Pairs (>|0.8|):\n")

for i in range(len(corr_matrix.columns)):
    for j in range(i):
        if abs(corr_matrix.iloc[i, j]) > 0.8:
            print(f"{corr_matrix.columns[i]} and {corr_matrix.columns[j]} -> {corr_matrix.iloc[i, j]:.2f}")

plt.figure(figsize=(6,4))
sns.boxplot(y=df["Price"])
plt.title("Boxplot of House Prices")
plt.show()

print("\nObservations:")
print("- Features with correlation above 0.8 indicate strong relationships.")
print("- Strongly correlated features may cause multicollinearity in ML models.")
print("- The boxplot shows an extreme high Price value (possible outlier).")
print("- Outliers can distort the mean and affect regression model performance.")
