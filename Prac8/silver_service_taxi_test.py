from silver_service_taxi import SilverServiceTaxi


def main():
    """ testing the SilverServiceTaxi"""
    taxi = SilverServiceTaxi("Fanciness taxi", 100, 1.28, 2)
    taxi.drive(18)
    print(taxi)
    print(taxi.get_fare())


if __name__ == '__main__':
    main()

