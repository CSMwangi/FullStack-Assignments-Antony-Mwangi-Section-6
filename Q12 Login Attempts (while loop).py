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
