import random

MIN_NUM = 1
MAX_NUM = 45
NUMS_PER_LINE = 6
NUM_OF_LINES = 5

def generate_quick_pick():
    numbers = random.sample(range(MIN_NUM, MAX_NUM + 1), NUMS_PER_LINE)
    numbers.sort()
    return numbers

def print_quick_picks(num_of_picks):
    for _ in range(num_of_picks):
        quick_pick = generate_quick_pick()
        print(' '.join(map(str, quick_pick)))
num_of_picks = int(input("How many quick picks do you want to generate? "))
print_quick_picks(num_of_picks)
