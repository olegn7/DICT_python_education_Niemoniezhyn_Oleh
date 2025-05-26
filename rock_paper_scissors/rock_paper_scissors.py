import random

def load_ratings(filename):
    ratings = {}
    try:
        with open(filename, "r") as f:
            for line in f:
                name, score = line.split()
                ratings[name] = int(score)
    except FileNotFoundError:
        pass
    return ratings

def get_winners_and_losers(options, choice):
    n = len(options)
    idx = options.index(choice)
    rotated = options[idx+1:] + options[:idx]
    half = len(rotated) // 2
    losers = rotated[:half]    # эти проигрывают choice
    winners = rotated[half:]   # эти побеждают choice
    return winners, losers

def main():
    ratings = load_ratings("rating.txt")
    name = input("Enter your name: ")
    print(f"Hello, {name}")
    score = ratings.get(name, 0)

    options_input = input()
    if options_input.strip() == "":
        options = ["rock", "paper", "scissors"]
    else:
        options = options_input.strip().split(",")
    print("Okay, let's start")

    while True:
        user_choice = input()
        if user_choice == "!exit":
            print("Bye!")
            break
        elif user_choice == "!rating":
            print(f"Your rating: {score}")
        elif user_choice in options:
            computer_choice = random.choice(options)
            if user_choice == computer_choice:
                print(f"There is a draw ({computer_choice})")
                score += 50
            else:
                winners, losers = get_winners_and_losers(options, user_choice)
                if computer_choice in winners:
                    print(f"Sorry, but the computer chose {computer_choice}")
                else:
                    print(f"Well done. The computer chose {computer_choice} and failed")
                    score += 100
        else:
            print("Invalid input")

if __name__ == "__main__":
    main()
