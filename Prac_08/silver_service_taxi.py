"""
Nicholas West
Silver Service Taxi
24/11/2020

"""

from Prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    fall = 4.5

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        return "{} plus fall of ${:.2f}".format(super().__str__(),
                                                self.fall)

    def get_fare(self):
        return self.fall + super().get_fare()
