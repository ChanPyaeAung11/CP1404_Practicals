def main():

    password = input("Input the password: ")
    password_check(password)

    MENU = "\n MENU \n C - Convert Celsius to Fahrenheit \n F - Convert Fahrenheit to Celsius \n Q - Quit"
    print(MENU)
    choice = input(">>> ").upper()
    print(temperature_change(choice, MENU))

    score = num_check("Enter score: ")
    print(broken_score(score))


def password_check(password):
    for i in password:
        print("*", end="")


def temperature_change(choice, MENU):
    while choice != "Q":
        if choice == "C":
            ask_celsius = float(input("Celsius: "))
            calc_fahrenheit = ask_celsius * 9 / 5 + 32
            return "Result: {:.2f} F".format(calc_fahrenheit)
        elif choice == "F":
            ask_fahrenheit = float(input("Fahrenheit: "))
            calc_celsius = 5/9 * (ask_fahrenheit - 32)
            return "Result: {:.2f} C ".format(calc_celsius)
        else:
            print("Invalid Option")
        choice = input(">>> ").upper()
    print("Thank you.")


def broken_score(score):
    if 0 > score or score > 100:
        return "Invalid score"
    elif 50 <= score <= 90:
        return "Passable"
    elif score > 90:
        return "Excellent"
    else:
        return "Bad"


def num_check(prompt):
    while True:
        try:
            score = float(input(prompt))
            return score
        except ValueError:
            print("Enter numbers only")


main()
