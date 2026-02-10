file = open("sample.txt", "w")
file.write("hello,this is a text file.")
file.close()

file = open("sample.txt", "r")
content = file.read()
print(content)
file.close()

with open("sample.txt", "r")as file:
    content = file.read()
print(content)
with open("sample.txt", "a") as file:
    file.write("second data added\n")

with open("sample.txt", "r") as file:
    for line in file:
        print(line.strip()) 




















