import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
income_data = np.random.exponential(scale=50000, size=1000)

sample_means = []

for _ in range(1000):
    sample = np.random.choice(income_data, size=30, replace=True)
    sample_mean = np.mean(sample)
    sample_means.append(sample_mean)

plt.figure(figsize=(10,6))
plt.hist(sample_means, bins=30, color='skyblue', edgecolor='black')
plt.title("Histogram of 1000 Sample Means (n=30)")
plt.xlabel("Sample Mean")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

print("Observation: Even though original income data is heavily skewed,")
print("the histogram of sample means looks approximately Normal (bell-shaped).")