password = "Admin123"
max_attempts = 3

for attempt in range(max_attempts):
    user_password = input("Enter Password: ")

    if user_password == password:
        print("Access Granted")
        break
    else:
        print("Incorrect Password")

if user_password != password:
    print("Account Locked")