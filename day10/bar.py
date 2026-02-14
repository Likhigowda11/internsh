import matplotlib.pyplot as plt

months = [1, 2, 3, 4, 5]
sales = [100, 150, 200, 180, 220]

plt.plot(months, sales, label="Sales")

plt.title("Monthly Sales Report",fontsize=12)
plt.xlabel("Month",color="blue")
plt.ylabel("Sales Amount")
plt.legend() #A legend explains what each line, color, or marker represents.
plt.grid(True)

plt.show()
import matplotlib.pyplot as plt

x = [1,2,3,4]
y1 = [10,20,25,30]
y2 = [5,15,20,25]

plt.figure(figsize=(8,4))

# First subplot
plt.subplot(1,2,1)
plt.plot(x, y1)
plt.title("Line Plot")

# Second subplot
plt.subplot(1,2,2)
plt.bar(x, y2)
plt.title("Bar Chart")

plt.tight_layout()
plt.show()