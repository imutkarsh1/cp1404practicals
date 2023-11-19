from silver_service_taxi import SilverServiceTaxi

def main():
    # Create a SilverServiceTaxi instance
    hummer_taxi = SilverServiceTaxi("Hummer", 200, 4)

    # Drive the taxi 18 km
    hummer_taxi.drive(18)

    # Print the details and the current fare
    print("Taxi Details:")
    print(hummer_taxi)
    print("Current Fare:", hummer_taxi.get_fare())

if __name__ == '__main__':
    main()
