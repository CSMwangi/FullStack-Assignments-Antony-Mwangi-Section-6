# 12 LOGIN ATTEMPTS (WHILE LOOP)
# This script allows up to 3 password attempts before locking the account.
# It uses a while loop with a break condition for successful login.

password = "Mwangi2030"
attempts = 0

while attempts < 3:
    user_input = input("Enter password: ")
    if user_input == password:
        print("Access granted")
        break
    else:
        print("Wrong password, try again")
        attempts += 1

if attempts == 3:
    print("Account locked.")

