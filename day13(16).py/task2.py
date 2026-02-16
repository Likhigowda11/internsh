import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "SquareFootage": [800, 1200, 1500, 2000, 2500, 3000, 3500, 4000],
    "Price": [150000, 200000, 250000, 300000, 350000, 450000, 500000, 600000],
    "Location": ["Urban", "Urban", "Suburban", "Suburban", "Suburban", "Urban", "Rural", "Rural"]
}

df = pd.DataFrame(data)

sns.set(style="whitegrid")

sns.scatterplot(x="SquareFootage", y="Price", data=df)
plt.title("Square Footage vs Price")
plt.show()

sns.boxplot(x="Location", y="Price", data=df)
plt.title("Price Distribution by Location")
plt.show()

