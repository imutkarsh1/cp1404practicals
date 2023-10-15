def extract_name_from_email(email):
    return email.split('@')[0].replace('.', ' ').title()

def main():
    user_data = {}

    while True:
        email = input("Email: ")

        if not email:
            break

        name = extract_name_from_email(email)

        is_name_correct = input(f"Is your name {name}? (Y/n) ").lower()

        if is_name_correct in ['', 'y']:
            user_data[email] = name
        else:
            name = input("Name: ")
            user_data[email] = name

    for email, name in user_data.items():
        print(f"{name} ({email})")

if __name__ == "__main__":
    main()
