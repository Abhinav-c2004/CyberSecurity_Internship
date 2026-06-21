employees = ["John", "Alice", "David", "Sophia", "Michael"]

name = input("Enter employee name to search: ")

found = False

for employee in employees:
    if employee.lower() == name.lower():
        found = True
        break

if found:
    print("Record Found")
else:
    print("Record Not Found")