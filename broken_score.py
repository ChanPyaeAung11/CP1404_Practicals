import random


def main():
    score = random.randint(0, 105)
    print(score)
    print(broken_score(num_check(random.randint(0, 105))))


def broken_score(score):
    if 0 > score or score > 100:
        return "Invalid score"
    elif 50 <= score <= 90:
        return "Passable"
    elif score > 90:
        return "Excellent"
    else:
        return "Bad"


def num_check(score):
    while True:
        try:
            score = int(score)
            return score
        except ValueError:
            print("Enter integers only")


main()
