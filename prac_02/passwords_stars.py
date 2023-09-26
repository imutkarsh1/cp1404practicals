def get_password(min_length):
    while True:
        password = input("Please enter a password: ")
        if len(password) >= min_length:
            return password
        else:
            print(f"Password must be at least {min_length} characters long. Try again.")
def print_asterisks(password):
    print('*' * len(password))
def main():
    min_length = 8
    password = get_password(min_length)
    print_asterisks(password)
if __name__ == "__main__":
    main()
