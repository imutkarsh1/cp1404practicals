def celsius_to_fahrenheit(celsius):
    return celsius * 9.0 / 5 + 32
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9
MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
def get_valid_choice():
    while True:
        choice = input(">>> ").upper()
        if choice in {'C', 'F', 'Q'}:
            return choice
        else:
            print("Invalid option. Please choose C, F, or Q.")
choice = get_valid_choice()
while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"Result: {fahrenheit:.2f} F")
    elif choice == "F":
        fahrenheit = float(input("Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"Result: {celsius:.2f} C")
    print(MENU)
    choice = get_valid_choice()
print("Thank you.")