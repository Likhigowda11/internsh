filename = input("Enter the file name: ")
try:
  file = open(filename, "r")
  content = file.read()
  print(content)
  file.close()
except FileNotFoundError:
  print("Error: Oops!That file doesn't exist yet.")