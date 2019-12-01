def main():

    password = password_count(input("Input the password: "))
    password_check(password)


def password_count(password):
    while len(password) < 6:
        password = password_count(input("Password must be at least 6 words. \n >>>"))
    return password


def password_check(password):
    for i in password:
        print("*", end="")


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
