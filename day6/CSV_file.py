import csv

# Open the CSV file in read mode
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    #next(reader) 
    # Read and print each row
    for row in reader:   
        print(row)