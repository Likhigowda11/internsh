name = input("Enter your name: ")
age = input("Enter your current age: ")
age = int(age)
age_2030 = age + 4

print("Hey", name + ", you will be", age_2030, "years old in 2030!")

total_bill = float(input("Enter the total bill amount: "))
people = int(input("Enter the number of people: "))

share = total_bill / people

print("Total Bill:", total_bill)
print("Each person pays:", share)

print(type(total_bill))
print(type(people))
print(type(share))

item_name = "iphone"
quantity = 2
price = 89999.99
in_stock = True

print("Item:", item_name, "Qty:", quantity, "Price:", price, "Available:", in_stock)

total_cost = quantity * price
print("Total Cost:", total_cost)