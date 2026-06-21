first_name = input("Enter First Name: ").lower()
last_name = input("Enter Last Name: ").lower()
birth_year = input("Enter Birth Year: ")

year_last_two = birth_year[-2:]

print("\nUsername Suggestions:")
print(first_name + last_name + birth_year)
print(first_name[0] + "." + last_name + year_last_two)
print(last_name + "_" + first_name)
print(first_name + "_" + year_last_two)
print(last_name + first_name[0] + birth_year)