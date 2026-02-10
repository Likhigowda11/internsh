friend_a = {"Python", "Cooking", "Hiking", "Movies"}
friend_b = {"Hiking", "Gaming", "Photography", "Python"}
all_interests = friend_a | (friend_b) 
print("All interests:", all_interests)
common_interests = friend_a & (friend_b)
print("Common interests:", common_interests)
unique_to_friend_a = friend_a - (friend_b) 
unique_to_friend_b = friend_b - (friend_a)
print("Interests unique to friend_a:", unique_to_friend_a)
print("Interests unique to friend_b:", unique_to_friend_b)