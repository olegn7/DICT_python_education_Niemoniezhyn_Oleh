import random

def input_pencils():
    while True:
        print("How many pencils would you like to use:")
        pencils = input("> ")
        if not pencils.isdigit():
            print("The number of pencils should be numeric")
            continue
        pencils = int(pencils)
        if pencils <= 0:
            print("The number of pencils should be positive")
            continue
        return pencils

def input_first_player(names):
    while True:
        print(f"Who will be the first ({names[0]}, {names[1]}):")
        player = input("> ")
        if player not in names:
            print(f"Choose between '{names[0]}' and '{names[1]}'")
            continue
        return player

def input_take(pencils_left):
    while True:
        taken = input()
        if taken not in ('1', '2', '3'):
            print("Possible values: '1', '2' or '3'")
            continue
        taken = int(taken)
        if taken > pencils_left:
            print("Too many pencils were taken")
            continue
        return taken

def bot_move(pencils_left):
    if pencils_left == 1:
        return 1
    if pencils_left % 4 == 1:
        return random.choice([1, 2, 3])
    remainder = pencils_left % 4
    if remainder == 0:
        return 3
    elif remainder == 3:
        return 2
    else:
        return 1

def main():
    players = ["John", "Jack"]
    pencils = input_pencils()
    current = input_first_player(players)
    other = players[1] if current == players[0] else players[0]

    while pencils > 0:
        print('|' * pencils)
        print(f"{current}'s turn:")
        if current == "Jack":
            taken = bot_move(pencils)
            print(taken)
        else:
            taken = input_take(pencils)
        pencils -= taken
        if pencils == 0:
            print(f"{other} won!")
            break
        current, other = other, current

if __name__ == "__main__":
    main()
