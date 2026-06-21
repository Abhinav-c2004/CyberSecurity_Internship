

stored_username = "admin"
stored_password = "password123"

username = input("Enter Username: ")
password = input("Enter Password: ")

if username == stored_username and password == stored_password:
    print("Login Successful")
else:
    print("Invalid Credentials")