import random

def get_result(score):
    if 0 <= score <= 100:
        if score >= 90:
            return "Excellent"
        elif score >= 50:
            return "Passable"
        else:
            return "Bad"
    else:
        return "Invalid score"
def main():
    user_score = float(input("Enter score: "))
    result = get_result(user_score)
    print(result)
    random_score = random.randint(0, 100)
    result = get_result(random_score)
    print(f"Random score: {random_score}, Result: {result}")
if __name__ == "__main__":
    main()
