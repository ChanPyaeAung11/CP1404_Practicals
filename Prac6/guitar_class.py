
class Guitar:

    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    '''Return a string that represents Guitar'''

    def __str__(self):
        return "{} ({})  : ${}".format(self.name, self.year, self.cost)

    def get_age(self):
        """Find the age of a guitar"""
        return 2017 - self.year

    def is_vintage(self):
        """Check to see if a guitar is vintage"""
        return self.get_age() >= 50