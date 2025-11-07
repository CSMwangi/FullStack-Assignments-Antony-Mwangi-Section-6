day = int(input("Enter a number (1–7): "))

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5 | 6 | 7:
        print("Looking forward to the weekend!")
    case _:
        print("Invalid day number.")
