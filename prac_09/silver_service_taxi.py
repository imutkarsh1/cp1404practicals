from taxi import Taxi

class SilverServiceTaxi(Taxi):
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def calculate_fare(self):
        """Calculate the fare for the current trip."""
        return super().calculate_fare() + self.flagfall

    def __str__(self):
        return super().__str__() + f" plus flagfall of ${self.flagfall:.2f}"
