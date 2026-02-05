raw_logs = ["id01","id02","id01","id05","id02","id08","id01"]
unique_users = set(raw_logs)
print(unique_users)
print("Is id05 present?", "id05" in unique_users)
print("total users:",len(raw_logs))
print("unique users:",len(unique_users))