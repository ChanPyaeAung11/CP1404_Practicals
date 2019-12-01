def main():

    print(broken_score(num_check("Enter score: ")))


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
            score = int(input(prompt))
            return score
        except ValueError:
            print("Enter integers only")


main()
