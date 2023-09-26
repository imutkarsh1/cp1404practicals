from score import get_result
def get_valid_score():
    while True:
        try:
            score = float(input("Enter a valid score (0-100): "))
            if 0 <= score <= 100:
                return score
            else:
                print("Invalid score. Please enter a number between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")
def show_stars(score):
    print('*' * int(score))
def print_result(score):
    result = get_result(score)
    print(f"The result is: {result}")
def main():
    score = get_valid_score()
    while True:
        print("\nMenu:")
        print("(G)et a valid score")
        print("(P)rint result")
        print("(S)how stars")
        print("(Q)uit")
        choice = input("Choose an option: ").upper()
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print_result(score)
        elif choice == "S":
            show_stars(score)
        elif choice == "Q":
            print("Farewell! Have a great day!")
            break
        else:
            print("Invalid option. Please choose a valid option.")
if __name__ == "__main__":
    main()