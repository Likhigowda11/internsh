import pandas as pd

usernames = pd.Series([' Alice ', 'bOB', ' Charlie_Data ', 'daisy'])
cleaned_usernames = usernames.str.strip().str.lower()

contains_a = cleaned_usernames.str.contains('a')

print("Original Series:")
print(usernames)

print("\nCleaned Series:")
print(cleaned_usernames)

print("\nNames containing letter 'a':") 
print(contains_a)
