Name = (input("Enter your name: "))
Daily_goal = (input("Enter your daily goal: "))

with open("journal.txt", "a") as file:
    file.write(f"Name: {Name}, Daily Goal: {Daily_goal}\n")
    file.write("\n")  # Add a newline for separation between entries