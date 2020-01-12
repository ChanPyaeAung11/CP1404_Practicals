from unreliable_car import UnreliableCar

""" testing UnreliableCar """


def main():
    # made cars with two different reliabilities
    good_car = UnreliableCar("Toyota", 100, 90)
    bad_car = UnreliableCar("BMW", 100, 10)

    # drive 10 times
    # print out distance both cars drive
    for i in range(1, 11):
        print("Driving {} km".format(i))
        print("{} {}".format(good_car.name, good_car.drive(i)))
        print("{} {}".format(bad_car.name, bad_car.drive(i)))
        print()
    print(good_car)
    print(bad_car)


if __name__ == '__main__':
    main()
