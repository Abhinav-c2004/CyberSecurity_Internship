website = input("Enter Website Name: ")
username = input("Enter Username: ")
password = input("Enter Password: ")


with open("password_vault.txt", "a") as file:
    file.write("Website: " + website + "\n")
    file.write("Username: " + username + "\n")
    file.write("Password: " + password + "\n")
    file.write("-" * 30 + "\n")

print("\nRecord Saved Successfully!")


print("\nSaved Records:")
print("-" * 30)

with open("password_vault.txt", "r") as file:
    print(file.read())