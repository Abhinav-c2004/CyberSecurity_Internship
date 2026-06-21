N = int(input("Enter a number: "))

sum_numbers = 0
even_count = 0
odd_count = 0

for i in range(1, N + 1):
    sum_numbers += i

    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Sum =", sum_numbers)
print("Even Numbers =", even_count)
print("Odd Numbers =", odd_count)