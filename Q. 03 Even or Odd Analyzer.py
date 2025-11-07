# 3 EVEN OR ODD ANALYZER
# This script checks numbers from 1 to 10 and prints whether each number is even or odd.
# It uses a for loop and the modulus operator (%) to test for evenness.

numbers = list(range(1, 11))

for num in numbers:
    if num % 2 == 0:
        print(f"Even number: {num}")
    else:
        print(f"Odd number: {num}")

