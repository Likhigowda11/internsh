import numpy as np
import pandas as pd

np.random.seed(42)

scores = np.random.normal(loc=70, scale=10, size=100)
scores = np.append(scores, [20, 150])

df = pd.DataFrame({"Exam_Score": scores})

mean_value = df["Exam_Score"].mean()
std_value = df["Exam_Score"].std()

print("Mean (μ):", round(mean_value, 2))
print("Standard Deviation (σ):", round(std_value, 2))

df["z_score"] = (df["Exam_Score"] - mean_value) / std_value

outliers = df[np.abs(df["z_score"]) > 3]

print("\nOutliers (|Z| > 3):")
print(outliers)