# 6 LOGIN SIMULATION
# This program simulates a basic login system.
# It checks if the entered email and password match stored credentials.


stored_email = "antony@gmail.com"
stored_password = "12345"

email = input("Enter your email: ")
password = input("Enter your password: ")

if email == stored_email and password == stored_password:
    print("Login successful!")
else:
    print("Invalid credentials!")

