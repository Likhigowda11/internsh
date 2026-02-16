import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis
import numpy as np

data = {
    "Price": [250000, 300000, 280000, 500000, 450000, 600000, 750000, 900000, 1200000, 1500000, 350000, 400000, 1000000, 2000000],
    "Area": [1200, 1500, 1300, 2000, 1800, 2200, 2500, 3000, 3500, 4000, 1600, 1700, 3200, 5000],
    "Bedrooms": [2, 3, 2, 4, 3, 4, 5, 5, 6, 7, 3, 3, 6, 8],
    "City": ["Chennai", "Mumbai", "Delhi", "Chennai", "Mumbai",
             "Delhi", "Chennai", "Mumbai", "Delhi", "Chennai",
             "Mumbai", "Delhi", "Chennai", "Delhi"]
}

df = pd.DataFrame(data)
print(df.head())

plt.figure()
sns.histplot(df["Price"], kde=True)
plt.title("Price Distribution")
plt.show()

price_skewness = skew(df["Price"])
price_kurtosis = kurtosis(df["Price"])

print("Skewness:", price_skewness)
print("Kurtosis:", price_kurtosis)

plt.figure()
sns.countplot(x="City", data=df)
plt.title("City Distribution")
plt.show()