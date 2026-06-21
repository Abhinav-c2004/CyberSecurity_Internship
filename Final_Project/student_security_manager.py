import os

FILE_NAME = "students.txt"

# -------------------------------
# Login Validation
# -------------------------------
USERNAME = "admin"
PASSWORD = "admin123"


def login():
    print("===== LOGIN =====")

    user = input("Username: ")
    pwd = input("Password: ")

    if user == USERNAME and pwd == PASSWORD:
        print("Login Successful!\n")
        return True
    else:
        print("Invalid Credentials!")
        return False


# -------------------------------
# Add Student
# -------------------------------
def add_student():
    name = input("Enter Student Name: ")
    sid = input("Enter Student ID: ")
    branch = input("Enter Branch: ")
    email = input("Enter Email: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{sid},{name},{branch},{email}\n")

    print("Student Added Successfully!\n")


# -------------------------------
# View Students
# -------------------------------
def view_students():
    if not os.path.exists(FILE_NAME):
        print("No Records Found!\n")
        return

    with open(FILE_NAME, "r") as file:
        records = file.readlines()

    if len(records) == 0:
        print("No Students Available.\n")
        return

    print("\n===== STUDENT RECORDS =====")

    for record in records:
        sid, name, branch, email = record.strip().split(",")

        print(f"ID     : {sid}")
        print(f"Name   : {name}")
        print(f"Branch : {branch}")
        print(f"Email  : {email}")
        print("-" * 30)


# -------------------------------
# Search Student
# -------------------------------
def search_student():
    key = input("Enter Student Name or ID: ")

    found = False

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for record in file:
                sid, name, branch, email = record.strip().split(",")

                if key == sid or key.lower() == name.lower():
                    print("\nRecord Found")
                    print(f"ID     : {sid}")
                    print(f"Name   : {name}")
                    print(f"Branch : {branch}")
                    print(f"Email  : {email}")
                    found = True

    if not found:
        print("Student Not Found!\n")


# -------------------------------
# Delete Student
# -------------------------------
def delete_student():
    sid = input("Enter Student ID to Delete: ")

    if not os.path.exists(FILE_NAME):
        print("No Records Found!")
        return

    records = []

    deleted = False

    with open(FILE_NAME, "r") as file:
        for record in file:
            data = record.strip().split(",")

            if data[0] != sid:
                records.append(record)
            else:
                deleted = True

    with open(FILE_NAME, "w") as file:
        file.writelines(records)

    if deleted:
        print("Student Deleted Successfully!")
    else:
        print("Student Not Found!")


# -------------------------------
# Security Assessment
# -------------------------------
security_scores = []


def security_assessment():
    score = 0

    mfa = input("Is MFA Enabled? (yes/no): ").lower()

    if mfa == "yes":
        score += 25

    length = int(input("Password Length: "))

    if length >= 12:
        score += 25
    elif length >= 8:
        score += 15

    update = input("System Updated? (yes/no): ").lower()

    if update == "yes":
        score += 25

    antivirus = input("Antivirus Installed? (yes/no): ").lower()

    if antivirus == "yes":
        score += 25

    security_scores.append(score)

    print(f"\nSecurity Score: {score}/100")

    if score >= 90:
        print("Status: Excellent")
    elif score >= 70:
        print("Status: Good")
    elif score >= 50:
        print("Status: Moderate")
    else:
        print("Status: Poor")


# -------------------------------
# Generate Report
# -------------------------------
def generate_report():
    total_students = 0

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            total_students = len(file.readlines())

    print("\n===== REPORT =====")
    print("Total Students:", total_students)

    print("Security Scores:", security_scores)

    if len(security_scores) > 0:
        avg = sum(security_scores) / len(security_scores)
        print("Average Security Score:", round(avg, 2))

        poor = 0

        for score in security_scores:
            if score < 50:
                poor += 1

        print("Students with Poor Security Ratings:", poor)
    else:
        print("No Security Assessments Available")


# -------------------------------
# Password Strength Checker
# -------------------------------
def password_checker():
    password = input("Enter Password: ")

    score = 0

    if len(password) >= 8:
        score += 1

    if any(c.isupper() for c in password):
        score += 1

    if any(c.islower() for c in password):
        score += 1

    if any(c.isdigit() for c in password):
        score += 1

    if any(not c.isalnum() for c in password):
        score += 1

    if score == 5:
        print("Strong Password")
    elif score >= 3:
        print("Medium Password")
    else:
        print("Weak Password")


# -------------------------------
# Username Generator
# -------------------------------
def username_generator():
    name = input("Enter Full Name: ")

    username = name.lower().replace(" ", "") + "123"

    print("Generated Username:", username)


# -------------------------------
# Security Menu
# -------------------------------
def cyber_tools():
    while True:
        print("\n===== CYBER SECURITY TOOLS =====")
        print("1. Password Strength Checker")
        print("2. Username Generator")
        print("3. Back")

        choice = input("Enter Choice: ")

        if choice == "1":
            password_checker()

        elif choice == "2":
            username_generator()

        elif choice == "3":
            break

        else:
            print("Invalid Choice!")


# -------------------------------
# Main Menu
# -------------------------------
def main():
    if not login():
        return

    while True:
        print("\n==========================")
        print(" Student Security Manager ")
        print("==========================")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Security Assessment")
        print("6. Generate Report")
        print("7. Cyber Security Tools")
        print("8. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            delete_student()

        elif choice == "5":
            security_assessment()

        elif choice == "6":
            generate_report()

        elif choice == "7":
            cyber_tools()

        elif choice == "8":
            print("Exiting Program...")
            break

        else:
            print("Invalid Choice!")


main()