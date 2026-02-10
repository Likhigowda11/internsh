import numpy as np

arr =  np.arange(40,50,3)
print("Array of numbers:",arr)

print(arr.shape)
arr_1 =np.arange(1,17).reshape(4,4)
print(arr_1)
arr = np.linspace(0, 2, 5)
print(arr)

arr = np.random.rand(2, 2)
print(arr)
#rand() → Only floats in [0, 1)-generates a 2×2 array (matrix) 
# filled with random numbers between 0 and 1.
arr = np.arange(12)
reshaped = arr.reshape(3, 4)
print(reshaped)
import numpy as np

a = np.array([[1, 2]])
b = np.array([[3, 4]])

vstacked = np.vstack((a, b))
print(vstacked)