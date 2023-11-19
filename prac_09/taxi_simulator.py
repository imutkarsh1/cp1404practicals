from taxi_module import Taxi
from silver_service_taxi_module import SilverServiceTaxi

def main():
    fleet = [
        Taxi("GreenCab", 100),
        SilverServiceTaxi("LuxLimo", 100, 2),
        SilverServiceTaxi("BigHummer", 200, 4)
    ]
    selected_taxi = None
    total_cost = 0.0

    print("Let's roll!")
    while True:
        print("q)uit, c)hoose taxi, d)rive")
        user_choice = input(">>> ").lower()
        if user_choice == 'q':
            break
        elif user_choice == 'c':
            print("Available Taxis:")
            show_taxis(fleet)
            taxi_selection = int(input("Select taxi: "))
            try:
                selected_taxi = fleet[taxi_selection]
            except IndexError:
                print("Invalid taxi selection")
        elif user_choice == 'd':
            if selected_taxi:
                distance_traveled = float(input("Drive how far? "))
                selected_taxi.drive(distance_traveled)
                trip_expense = selected_taxi.get_fare()
                print(f"Your {selected_taxi.name} trip cost you ${trip_expense:.2f}")
                total_cost += trip_expense
                selected_taxi.start_fare()
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid option")
        print(f"Total bill: ${total_cost:.2f}")

    print(f"Total trip cost: ${total_cost:.2f}")
    print("Updated Fleet:")
    show_taxis(fleet)

def show_taxis(taxis):
    for i, cab in enumerate(taxis):
        print(f"{i} - {cab}")

if __name__ == '__main__':
    main()
