from taxi import Taxi


def main():
    test_taxi = Taxi("Prius 1", 100, 1.23)  # gives the car name, units of fuel and price of fuel
    test_taxi.drive(40)     # drives 40km distance
    print(test_taxi)        # print taxi's detail and current fare
    print("${}".format(test_taxi.get_fare()))   # prints out the fare of the ride
    test_taxi.start_fare()      # starts the fare back to 0
    test_taxi.drive(100)    # drives 100km distance
    print(test_taxi)
    print("${}".format(test_taxi.get_fare()))


main()
