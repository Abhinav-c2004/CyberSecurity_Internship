def display_student_info(name, roll_no, branch, semester):
    print("\nStudent Information")
    print("Name:", name)
    print("Roll No:", roll_no)
    print("Branch:", branch)
    print("Semester:", semester)


name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")
branch = input("Enter Branch: ")
semester = input("Enter Semester: ")


display_student_info(name, roll_no, branch, semester)