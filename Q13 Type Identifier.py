# 13 TYPE IDENTIFIER
# This program asks the user to enter any value and identifies its data type.
# It uses basic type checking logic with isinstance and input validation.

value = input("Enter any value: ")

print("Raw input:", value)

if value.isdigit():
    print("Data type: int")
elif value.replace('.', '', 1).isdigit():
    print("Data type: float")
else:
    print("Data type: str")

