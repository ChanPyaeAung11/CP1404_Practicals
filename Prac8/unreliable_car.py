from car import Car
from random import randint


class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        # drive based on the reliability
        random_number = randint(0, 10)
        if random_number < self.reliability:
            distance = 0
        distance_driven = super().drive(distance)  # tell parent class that distance is 0
        return distance_driven
