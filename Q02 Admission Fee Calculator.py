# 2️ ADMISSION FEE CALCULATOR
# This program calculates the admission fee based on the user's age.
# It demonstrates conditional logic and formatted string output.

name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age < 12:
    fee = 100
elif 12 <= age <= 18:
    fee = 200
else:
    fee = 300

print(f"{name} pays {fee} KES for admission.")

