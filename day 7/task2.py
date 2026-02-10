import numpy as np

data = np.arange(24)
reshaped_data = data.reshape(4, 3, 2)
final_data = reshaped_data.transpose(0, 2, 1)
print("Final Shape:", final_data.shape)
print("Final Array:")
print(final_data)