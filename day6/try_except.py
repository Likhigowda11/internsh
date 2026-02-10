try:
    file = open("missing_file.txt", "r")
    content = file.read()
    print(content)
    file.close()

except FileNotFoundError:
    print("Error: The file does not exist. Please check the file name or path.")

except PermissionError:
    print("Error: You do not have permission to access this file.")

except Exception as e:
    print("An unexpected error occurred:", e)