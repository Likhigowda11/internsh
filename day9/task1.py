import pandas as pd 

product = pd.Series([700, 150, 300], index=['Laptop', 'Mouse', 'Keyboard'])
print(product)

print(product['Laptop'])
print(product[0:2])
