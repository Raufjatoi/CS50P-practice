import random


def main():
    level = get_level()
    score = 0
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        correct_answer = x + y
        attempts = 0
        while True:
            user_answer = input(f"{x} + {y} = ")
            if user_answer.isdigit():
                if int(user_answer) == correct_answer:
                    score += 1
                    
                    break
                else:
                    attempts += 1
                    if attempts == 3:
                        print(f"{correct_answer}")
                        break
                    else:
                        print("EEE")
            else:
                print("EEE..")
    print(f"Score: {score}/10")


def get_level():
    while True:
        level = input("Enter the level (1, 2, or 3): ")
        if level in ['1', '2', '3']:
            return int(level)
        else:
            print("Invalid level. Please enter 1, 2, or 3.")


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError("Invalid level. Level must be 1, 2, or 3.")


if __name__ == "__main__":
    main()
