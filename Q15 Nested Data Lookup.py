# 15 NESTED DATA LOOKUP
# This program retrieves a family member’s details (name and birth year) from a nested dictionary.
# It practices nested data access and condition checking.

myFamily = {
    "father": {"name": "Antony Mwangi", "year": 2002},
    "mother": {"name": "Naomi Wangui", "year": 2005}
}

person = input("Enter 'father' or 'mother': ").lower()

if person in myFamily:
    print(f"Name: {myFamily[person]['name']}, Year of birth: {myFamily[person]['year']}")
else:
    print("Family member not found.")

    

