MENU = "MENU \n C - Convert Celsius to Fahrenheit \n F - Convert Fahrenheit to Celsius \n Q - Quit"

print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "C":
        ask_celsius = float(input("Celsius: "))
        calc_fahrenheit = ask_celsius * 9 / 5 + 32
        print("Result: {:.2f} F".format(calc_fahrenheit))
    elif choice == "F":
        ask_fahrenheit = float(input("Fahrenheit: "))
        calc_celsius = 5/9 * (ask_fahrenheit - 32)
        print("Result: {:.2f} C ".format(calc_celsius))
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")