class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${'{:,.2f}'.format(self.cost)}"

    def get_age(self):
        current_year = 2022  # Assuming current year is 2022
        return current_year - self.year

    def is_vintage(self):
        return self.get_age() >= 50


# Example usage:
name = "Gibson L-5 CES"
year = 1922
cost = 16035.40

guitar = Guitar(name, year, cost)
print(guitar)
print(f"This guitar is {guitar.get_age()} years old.")
print(f"Is it vintage? {guitar.is_vintage()}")
