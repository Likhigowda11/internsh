total_bill = float(input("Enter the total bill amount: "))
people = int(input("Enter the number of people: "))

share = total_bill / people

print("Total Bill:", total_bill)
print("Each person pays:", share)

print(type(total_bill))
print(type(people))
print(type(share))