from guitar_class import Guitar

CURRENT_YEAR = 2017
def main():
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40

    guitar = Guitar(name, year, cost)
    Another_Guitar = Guitar("Another Guitar", 2012, 2152.65)

    print("{} - Expected {}. Got {}".format(guitar.name, 95, guitar.get_age()))
    print("{} - Expected {}. Got {}".format(Another_Guitar.name, 5, Another_Guitar.get_age()))
    print("{} is_vintage() - Expected {}. Got {}".format(guitar.name, True, guitar.is_vintage()))
    print("{} is_vintage() - Expected {}. Got {}".format(guitar.name, False, guitar.is_vintage()))

main()