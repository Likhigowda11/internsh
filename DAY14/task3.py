import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

X = np.array([1,2,3,4,5,6,7,8,9,10]).reshape(-1,1)
y = np.array([2,5,10,17,26,37,50,65,82,101])  

model = LinearRegression()
model.fit(X, y)

y_pred_linear = model.predict(X)

poly = PolynomialFeatures(degree=2)

X_poly = poly.fit_transform(X)

model_poly = LinearRegression()
model_poly.fit(X_poly, y)

y_pred_poly = model_poly.predict(X_poly)


r2_linear = r2_score(y, y_pred_linear)
print("R2 Score (Linear):", r2_linear)

r2_poly = r2_score(y, y_pred_poly)
print("R2 Score (Polynomial):", r2_poly)


plt.scatter(X, y, color="blue", label="Actual")

plt.plot(X, y_pred_linear, color="red", label="Linear Fit")

plt.plot(X, y_pred_poly, color="green", label="Polynomial Fit")

plt.legend()
plt.show()