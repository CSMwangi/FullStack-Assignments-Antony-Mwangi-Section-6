numbers = [4, 15, 23, 9, 12, 7, 18]
count = 0

for n in numbers:
    if n <= 10:
        continue
    print(f"Number greater than 10: {n}")
    count += 1

print(f"Total numbers greater than 10: {count}")
