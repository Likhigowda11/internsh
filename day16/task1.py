import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)

heights = np.random.normal(loc=170, scale=10, size=1000)
incomes = np.random.exponential(scale=50000, size=1000)
scores = 100 - np.random.exponential(scale=10, size=1000)
scores = np.clip(scores, 0, 100)

df = pd.DataFrame({
    "Heights": heights,
    "Incomes": incomes,
    "Scores": scores
})

def analyze_distribution(data, title):
    
    mean_value = data.mean()
    median_value = data.median()
    
    plt.figure(figsize=(7, 4))
    sns.histplot(data, kde=True, bins=30)
    
    plt.axvline(mean_value, color='red', linestyle='--', label=f"Mean = {mean_value:.2f}")
    plt.axvline(median_value, color='blue', linestyle='-', label=f"Median = {median_value:.2f}")
    
    plt.title(title)
    plt.legend()
    plt.show()
    
    print(f"\n{title}")
    print(f"Mean   : {mean_value:.2f}")
    print(f"Median : {median_value:.2f}")
    
    if mean_value > median_value:
        print("Observation: Mean > Median → Right-Skewed Distribution")
    elif mean_value < median_value:
        print("Observation: Mean < Median → Left-Skewed Distribution")
    else:
        print("Observation: Mean ≈ Median → Approximately Normal Distribution")

analyze_distribution(df["Heights"], "Human Heights (Normal Distribution)")
analyze_distribution(df["Incomes"], "Household Incomes (Right-Skewed)")
analyze_distribution(df["Scores"], "Easy Exam Scores (Left-Skewed)")