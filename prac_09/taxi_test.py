
from your_taxi_module import Taxi

my_taxi = Taxi("Prius 1", 100, 1.23)


my_taxi.drive(40)
print("Taxi Details:")
print(my_taxi)
print("Current Fare:", my_taxi.get_fare())

my_taxi.start_new_fare()

my_taxi.drive(100)
print("\nTaxi Details:")
print(my_taxi)
print("Current Fare:", my_taxi.get_fare())
