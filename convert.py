print("1. Celsius to Fahrenheit")
print("2. Kilometers to Miles")
print("3. Kilograms to Pounds")
print("4. Megabytes to Gigabytes")

choice = int(input("Enter your choice (1-4): "))

if choice == 1:
    c = float(input("Enter Celsius: "))
    f = (c * 9/5) + 32
    print("Fahrenheit =", f)

elif choice == 2:
    km = float(input("Enter Kilometers: "))
    miles = km * 0.621371
    print("Miles =", miles)

elif choice == 3:
    kg = float(input("Enter Kilograms: "))
    pounds = kg * 2.20462
    print("Pounds =", pounds)

elif choice == 4:
    mb = float(input("Enter Megabytes: "))
    gb = mb / 1024
    print("Gigabytes =", gb)

else:
    print("Invalid choice")
