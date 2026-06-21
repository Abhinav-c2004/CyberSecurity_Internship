
def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Division by zero is not allowed!"
    return a / b


print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter Choice: "))

num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))

if choice == 1:
    result = addition(num1, num2)
    print("Result:", result)

elif choice == 2:
    result = subtraction(num1, num2)
    print("Result:", result)

elif choice == 3:
    result = multiplication(num1, num2)
    print("Result:", result)

elif choice == 4:
    result = division(num1, num2)
    print("Result:", result)

else:
    print("Invalid Choice!")