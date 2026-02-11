import numpy as np

scores = np.random.randint(50, 101, size=(5, 3))
subject_mean = scores.mean(axis=0)
centered_scores = scores - subject_mean

print("Original Scores:\n", scores)
print("\nSubject-wise Mean:\n", subject_mean)
print("\nCentered Scores (After Normalization):\n", centered_scores)



data = np.array([[10,20,30],[40,50,60]])
print(np.mean(data))
print(np.mean(data,axis=0))

import numpy as np
data = np.array([10, 20, 30, 40, 50])
median_value = np.median(data)
print("Median:", median_value)

import numpy as np
data = np.array([10, 20, 30, 40, 50])
std_value = np.std(data)
print("Standard Deviation:", std_value)
