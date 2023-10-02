is_finished = False
result = None

while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        is_finished = True
    except ValueError:  # Catch the ValueError
        print("Please enter a valid integer.")

print("Valid result is:", result)