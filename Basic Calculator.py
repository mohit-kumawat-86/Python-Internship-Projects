print(""" 
1. Addition
2. Subtraction
3. Multiplication
4. Division 
5. Kilogram to Pounds
6. Celsius to Fahrenheit
7. Hours to Minutes
8. Miles to Kilometers
9. Meters to Kilometers
10. Exit
""")

while True:
    choice = input("Enter Your Choice: ")

    # ---------------- BASIC OPERATIONS ----------------
    if choice == "1":
        try:
            num1 = float(input("Enter Number 1: "))
            num2 = float(input("Enter Number 2: "))
        except ValueError:
            print("Please enter valid numbers!")
            continue
        print("Addition is", num1 + num2)

    elif choice == "2":
        try:
            num1 = float(input("Enter Number 1: "))
            num2 = float(input("Enter Number 2: "))
        except ValueError:
            print("Please enter valid numbers!")
            continue
        print("Subtraction is", num1 - num2)

    elif choice == "3":
        try:
            num1 = float(input("Enter Number 1: "))
            num2 = float(input("Enter Number 2: "))
        except ValueError:
            print("Please enter valid numbers!")
            continue
        print("Multiplication is", num1 * num2)

    elif choice == "4":
        try:
            num1 = float(input("Enter Number 1: "))
            num2 = float(input("Enter Number 2: "))
        except ValueError:
            print("Please enter valid numbers!")
            continue

        if num2 == 0:
            print("Cannot divide by zero!")
            continue

        print("Division is", num1 / num2)

    # ---------------- CONVERSIONS ----------------
    elif choice == "5":  # Kilogram → Pounds
        try:
            kg = float(input("Enter Kilograms: "))
        except ValueError:
            print("Please enter valid numbers!")
            continue
        pounds = kg * 2.20462
        print(kg, "Kilograms =", pounds, "Pounds")

    elif choice == "6":  # Celsius → Fahrenheit
        try:
            c = float(input("Enter Celsius: "))
        except ValueError:
            print("Please enter valid numbers!")
            continue
        f = (c * 9/5) + 32
        print(c, "Celsius =", f, "Fahrenheit")

    elif choice == "7":  # Hours → Minutes
        try:
            h = float(input("Enter Hours: "))
        except ValueError:
            print("Please enter valid numbers!")
            continue
        minutes = h * 60   
        print(h, "Hours =", minutes, "Minutes")

    elif choice == "8":  # Miles → Kilometers
        try:
            miles = float(input("Enter Miles: "))
        except ValueError:
            print("Please enter valid numbers!")
            continue
        km = miles * 1.60934
        print(miles, "Miles =", km, "Kilometers")

    elif choice == "9":  # Meters → Kilometers
        try:
            meters = float(input("Enter Meters: "))
        except ValueError:
            print("Please enter valid numbers!")
            continue
        km = meters / 1000
        print(meters, "meters =", km, "Kilometers")

    # ---------------- EXIT ----------------
    elif choice == "10":
        print("Exiting...")
        break

    else:
        print("Invalid choice")