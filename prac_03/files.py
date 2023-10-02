
user_name = input("Enter your name: ")

with open('name.txt', 'w') as file:
    file.write(user_name)

with open('name.txt', 'r') as file:
    name = file.read()
    print(f"Your name is {name}")


with open('numbers.txt', 'r') as file:
    first_number = int(file.readline())
    second_number = int(file.readline())
    total = first_number + second_number
    print(f"The total is {total}")
total = 0
with open('numbers.txt', 'r') as file:
    for line in file:
        total += int(line)

print(f"The total for all lines is {total}")
