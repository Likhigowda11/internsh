with open("data_cleaning.txt", "r")as file:
    for line in file:
        if line.strip():
            cleaned_line = line.strip()
            print(cleaned_line.lower())