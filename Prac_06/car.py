"""
Nicholas West
car class
24/11/2020
"""


class Car:

    def __init__(self, name="", fuel=0):
        self.name = name
        self.fuel = fuel
        self.odometer = 0

    def __str__(self):
        return "{}, fuel={}, odometer={}".format(self.name, self.fuel,
                                                 self.speedo)

    def add_fuel(self, amount):
        self.fuel += amount

    def driving(self, total_distance):
        if total_distance > self.fuel:
            distance = self.fuel
            self.fuel = 0
        else:
            self.fuel -= total_distance
        self.speedo += distance
        return distance
