marks = []

print("Enter marks of 5 students:")
for i in range(5):
    mark = int(input(f"Student {i+1}: "))
    marks.append(mark)

highest = max(marks)
lowest = min(marks)
average = sum(marks) / len(marks)

print("\nHighest Marks:", highest)
print("Lowest Marks:", lowest)
print("Average Marks:", average)