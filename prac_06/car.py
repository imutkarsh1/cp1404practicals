class Car:
    """Represent a Car object."""

    def __init__(self, fuel=0):
        """Initialise a Car instance."""
        self.fuel = fuel
        self._odometer = 0

    def add_fuel(self, amount):
        """Add amount to the car's fuel."""
        self.fuel += amount

    def drive(self, distance):
        """Drive the car a given distance."""
        if distance > self.fuel:
            distance = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
        self._odometer += distance
        return distance

    def get_odometer(self):
        """Return the car's odometer reading."""
        return self._odometer

def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return " ".join([s] * n)

def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in.
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length

def format_as_sentence(phrase):
    """
    Formats a given phrase as a sentence.
    >>> format_as_sentence('hello')
    'Hello.'
    >>> format_as_sentence('It is an ex parrot.')
    'It is an ex parrot.'
    >>> format_as_sentence('good morning')
    'Good morning.'
    """
    if not phrase.endswith('.'):
        phrase += '.'
    return phrase[0].upper() + phrase[1:]

def run_tests():
    """Run the tests on the functions."""
    assert repeat_string("Python", 1) == "Python"
    assert repeat_string("hi", 2) == "hi hi"

    test_car = Car()
    assert test_car.get_odometer() == 0, "Car does not set odometer correctly"

    default_car = Car()
    assert default_car.fuel == 0, "Car does not set default fuel value correctly"
    fuel_car = Car(fuel=10)
    assert fuel_car.fuel == 10, "Car does not set specified fuel value correctly"

run_tests()

# Uncomment the following line to run the doctests
# doctest.testmod()