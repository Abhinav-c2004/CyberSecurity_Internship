login_attempts = ["Success", "Failed", "Failed", "Success", "Failed", "Success"]

total_attempts = len(login_attempts)
successful_logins = 0
failed_logins = 0

for attempt in login_attempts:
    if attempt == "Success":
        successful_logins += 1
    else:
        failed_logins += 1

print("Total Attempts:", total_attempts)
print("Successful Logins:", successful_logins)
print("Failed Logins:", failed_logins)