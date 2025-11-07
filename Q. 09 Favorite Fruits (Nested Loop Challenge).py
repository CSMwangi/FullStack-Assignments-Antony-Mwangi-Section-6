# 9 FAVORITE FRUITS (NESTED LOOP CHALLENGE)
# This script prints every possible combination of colors and fruits.
# It demonstrates how nested loops work and counts total combinations.

colors = ["red", "green", "yellow"]
fruits = ["apple", "banana", "pear"]
count = 0

for color in colors:
    for fruit in fruits:
        print(f"{color} : {fruit}")
        count += 1

print(f"Total combinations: {count}")

