# 8 COLLECTION SORTER
# This program loops through a list of numbers and prints only those greater than 10.
# It also counts how many numbers meet that condition using a loop and continue statement.

numbers = [4, 15, 23, 9, 12, 7, 18]
count = 0

for n in numbers:
    if n <= 10:
        continue
    print(f"Number greater than 10: {n}")
    count += 1

print(f"Total numbers greater than 10: {count}")

