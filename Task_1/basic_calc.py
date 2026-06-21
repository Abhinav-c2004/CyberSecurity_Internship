
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))


addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2


print("\n----- Results -----")
print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")


if num2 != 0:
    division = num1 / num2
    print(f"Division: {division}")
else:
    print("Division: Cannot divide by zero")