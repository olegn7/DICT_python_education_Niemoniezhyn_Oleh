import random

def get_level():
    while True:
        print("Which level do you want? Enter a number:")
        print("1 - simple operations with numbers 2-9")
        print("2 - integral squares of 11-29")
        choice = input("> ")
        if choice == "1" or choice == "2":
            return int(choice)
        else:
            print("Incorrect format.")

def get_int_input():
    while True:
        user_input = input("> ")
        try:
            return int(user_input)
        except:
            print("Incorrect format.")

def ask_questions(level):
    correct = 0
    for _ in range(5):
        if level == 1:
            num1 = random.randint(2, 9)
            num2 = random.randint(2, 9)
            operation = random.choice(['+', '-', '*'])
            print(f"{num1} {operation} {num2}")
            answer = get_int_input()

            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            else:
                result = num1 * num2

        elif level == 2:
            num = random.randint(11, 29)
            print(num)
            answer = get_int_input()
            result = num ** 2

        if answer == result:
            print("Right!")
            correct += 1
        else:
            print("Wrong!")
    return correct

def save_result(name, score, level):
    level_descriptions = {
        1: "simple operations with numbers 2-9",
        2: "integral squares of 11-29"
    }
    with open("results.txt", "a") as f:
        f.write(f"{name}: {score}/5 in level {level} ({level_descriptions[level]}).\n")
    print('The results are saved in "results.txt".')

def main():
    level = get_level()
    score = ask_questions(level)
    print(f"Your mark is {score}/5.")

    print("Would you like to save your result to the file? Enter yes or no.")
    decision = input("> ").strip().lower()
    if decision in ["yes", "y"]:
        print("What is your name?")
        name = input("> ")
        save_result(name, score, level)

if __name__ == "__main__":
    main()
