# dashboard.py

import matplotlib.pyplot as plt

categories = ['Electronics', 'Clothing', 'Home']
sales = [300, 450, 200]

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
monthly_sales = [200, 250, 300, 400, 450]

plt.subplot(1, 2, 1)
plt.bar(categories, sales)
plt.title("Sales by Category")
plt.xlabel("Product Categories")
plt.ylabel("Sales")

plt.subplot(1, 2, 2)
plt.plot(months, monthly_sales, marker='o')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.tight_layout()

plt.show()
