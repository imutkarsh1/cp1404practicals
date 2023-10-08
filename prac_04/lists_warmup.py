# Initialize the list
numbers = [3, 1, 4, 1, 5, 9, 2]

# Values of the expressions
# numbers[0] - This is the first element of the list. It is 3.
# numbers[-1] - This is the last element of the list. It is 2.
# numbers[3] - This is the fourth element of the list. It is 1.
# numbers[:-1] - This is a slice of the list from the first element to the second-to-last element. It is [3, 1, 4, 1, 5, 9].
# numbers[3:4] - This is a slice containing only the fourth element. It is [1].
# 5 in numbers - Checks if 5 is in the list. It is True.
# 7 in numbers - Checks if 7 is in the list. It is False.
# "3" in numbers - Checks if the string "3" is in the list. It is False.
# numbers + [6, 5, 3] - Concatenates the list with [6, 5, 3]. It results in [3, 1, 4, 1, 5, 9, 2, 6, 5, 3].

# Change the first element of numbers to "ten" (the string, not the number 10)
numbers[0] = "ten"

# Change the last element of numbers to 1
numbers[-1] = 1

# Print all the elements from numbers except the first two (slice)
print(numbers[2:])

# Print whether 9 is an element of numbers
print(9 in numbers)
