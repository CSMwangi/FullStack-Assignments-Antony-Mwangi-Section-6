# 10 MEMBERSHIP CHECKER
# This program checks if a given car type exists in a list.
# It uses the 'in' operator to test membership in a collection.

cars = ["jeep", "suv", "sedan", "probox", "cx5","demio"]
car_name = input("Enter car name: ").lower()

if car_name in cars:
    print("We have that car type!")
else:
    print("Sorry, not available.")

    

