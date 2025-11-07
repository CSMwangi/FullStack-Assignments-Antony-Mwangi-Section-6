# 11 DICTIONARY ACCESS VALIDATION
# This program updates a user's profile verification status.
# It demonstrates how to modify values inside a Python dictionary based on user input.

user_profile = {
    "name": "Antony Mwangi",
    "email": "info.csmwangi@gmail.com",
    "verified": False
}

verified = input("Has the user verified their account? (yes/no): ").lower()

if verified == "yes":
    user_profile["verified"] = True
    print("Updated profile:", user_profile)
else:
    print("Verification pending.")
    

