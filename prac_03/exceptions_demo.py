#A ValueError will occur if the user enters something that can't be converted to an integer when using int(input())
#A ZeroDivisionError will occur if the user enters 0 as the denominator, as it's not possible to divide by zero.
#To avoid the possibility of a ZeroDivisionError, you can add a conditional statement to check if the denominator is zero before performing the divisi on.

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    if denominator == 0:
        print("Cannot divide by zero!")
    else:
        fraction = numerator / denominator
        print(fraction)

except ValueError:
    print("Numerator and denominator must be valid numbers!")

print("Finished.")