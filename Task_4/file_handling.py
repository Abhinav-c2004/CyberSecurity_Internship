# Read data from student_data.txt

try:
    file = open("student_data.txt", "r")
    
    print("Reading File...\n")
    content = file.read()
    print(content)
    
    file.close()

except FileNotFoundError:
    print("Error: student_data.txt file not found!")