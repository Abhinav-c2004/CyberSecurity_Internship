import csv


class Employee:
    def __init__(self, emp_id, name, department, designation, salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.designation = designation
        self.salary = salary


employees = []


def add_employee():
    emp_id = input("Employee ID: ")
    name = input("Employee Name: ")
    department = input("Department: ")
    designation = input("Designation: ")
    salary = float(input("Salary: "))

    employee = Employee(emp_id, name, department, designation, salary)
    employees.append(employee)

    print("\nEmployee Added Successfully.\n")


def view_employees():
    if not employees:
        print("\nNo employees found.\n")
        return

    print("-" * 80)
    print(f"{'ID':<10}{'Name':<20}{'Department':<15}{'Designation':<20}{'Salary':<10}")
    print("-" * 80)

    for emp in employees:
        print(
            f"{emp.emp_id:<10}{emp.name:<20}{emp.department:<15}"
            f"{emp.designation:<20}{emp.salary:<10.2f}"
        )

    print("-" * 80)


def search_employee():
    choice = input("\nSearch by (1-ID / 2-Name): ")

    if choice == "1":
        key = input("Enter Employee ID: ")
        for emp in employees:
            if emp.emp_id == key:
                display_employee(emp)
                return

    elif choice == "2":
        key = input("Enter Employee Name: ").lower()
        for emp in employees:
            if emp.name.lower() == key:
                display_employee(emp)
                return

    print("\nEmployee Not Found.\n")


def display_employee(emp):
    print("\nEmployee Details")
    print("--------------------------")
    print("ID:", emp.emp_id)
    print("Name:", emp.name)
    print("Department:", emp.department)
    print("Designation:", emp.designation)
    print("Salary:", emp.salary)
    print()


def update_employee():
    emp_id = input("Enter Employee ID: ")

    for emp in employees:
        if emp.emp_id == emp_id:
            emp.department = input("New Department: ")
            emp.designation = input("New Designation: ")
            emp.salary = float(input("New Salary: "))

            print("\nEmployee Updated Successfully.\n")
            return

    print("\nEmployee Not Found.\n")


def delete_employee():
    emp_id = input("Enter Employee ID: ")

    for emp in employees:
        if emp.emp_id == emp_id:
            employees.remove(emp)
            print("\nEmployee Deleted Successfully.\n")
            return

    print("\nEmployee Not Found.\n")


def salary_statistics():
    if not employees:
        print("\nNo employee records.\n")
        return

    salaries = [emp.salary for emp in employees]

    print("\nSalary Statistics")
    print("--------------------------")
    print("Highest Salary :", max(salaries))
    print("Lowest Salary  :", min(salaries))
    print("Average Salary :", sum(salaries) / len(salaries))
    print("Total Employees:", len(employees))
    print()


def export_data():
    filename = "employees.csv"

    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(
            ["Employee ID", "Name", "Department", "Designation", "Salary"]
        )

        for emp in employees:
            writer.writerow(
                [
                    emp.emp_id,
                    emp.name,
                    emp.department,
                    emp.designation,
                    emp.salary,
                ]
            )

    print("\nData exported successfully.\n")

    print("Reading data from file...\n")

    with open(filename, "r") as file:
        print(file.read())


def menu():
    while True:
        print("\n===== Employee Management System =====")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Search Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Salary Statistics")
        print("7. Export Data")
        print("8. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_employee()

        elif choice == "2":
            view_employees()

        elif choice == "3":
            search_employee()

        elif choice == "4":
            update_employee()

        elif choice == "5":
            delete_employee()

        elif choice == "6":
            salary_statistics()

        elif choice == "7":
            export_data()

        elif choice == "8":
            print("\nThank you!")
            break

        else:
            print("\nInvalid choice.\n")


menu()