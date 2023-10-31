from prac_06.car import Car

def main():
    """Demo test code to show how to use car class."""
    my_car = Car(180, "My Car")
    limo = Car(100, "Limo")
    limo.add_fuel(20)
    print(f"The amount of fuel in the car is: {limo.fuel}")
    distance_driven = limo.drive(115)
    print(f"The actual distance driven is: {distance_driven} km")
    print(my_car)
    print(limo)

main()
