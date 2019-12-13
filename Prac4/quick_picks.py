MIN = 1
MAX = 45
TIMES = 6
import random


def main():
    num_pick = int(input("How many quick picks: "))
    while num_pick <= 0:
        print("Input cannot be 0 or less than 0")
        num_pick = int(input("How many quick picks: "))
  
    for num in range(num_pick):
        numbers = []
        for i in range(TIMES):
            number = random.randint(MIN, MAX)
            while number in numbers:
                number = random.randint(MIN, MAX)
            numbers.append(number)
        numbers.sort()
        print(" ".join("{:2}".format(number) for number in numbers))


main()
