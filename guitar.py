class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def get_age(self, year):
        self.age = 2016 - year
        return self.age

    def is_vintage(self, year):
        age = self.get_age(year)
        if age >= 50:
            return True
        else:
            return False

    def __str__(self):
        return("{} ({}) : ${:.2f}".format(self.name, self.year, self.cost))