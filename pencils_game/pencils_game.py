while True:
    pencils = input("How many pencils would you like to use:\n")
    if not pencils.isdigit():
        print("The number of pencils should be numeric")
    elif int(pencils) == 0:
        print("The number of pencils should be positive")
    else:
        pencils = int(pencils)
        break

players = ["John", "Jack"]
while True:
    first = input(f"Who will be the first ({players[0]}, {players[1]}):\n")
    if first not in players:
        print(f"Choose between '{players[0]}' and '{players[1]}'")
    else:
        break

print("|" * pencils)
print(f"{first} is going first!")
def main():
    pencils = int(input("How many pencils would you like to use:\n> "))
    first_player = input("Who will be the first (John, Jack):\n> ")

    print('|' * pencils)
    current_player = first_player

    while pencils > 0:
        print(f"{current_player}'s turn:")
        take = int(input("> "))
        pencils -= take
        if pencils == 0:
            break
        print('|' * pencils)
        current_player = 'Jack' if current_player == 'John' else 'John'


if __name__ == "__main__":
    main()
players = ["John", "Jack"]

while True:
    pencils = input("How many pencils would you like to use:\n> ")
    if not pencils.isdigit():
        print("The number of pencils should be numeric")
    else:
        pencils = int(pencils)
        if pencils == 0:
            print("The number of pencils should be positive")
        else:
            break

first_player = input(f"Who will be the first ({players[0]}, {players[1]}):\n> ")
while first_player not in players:
    print(f"Choose between '{players[0]}' and '{players[1]}'")
    first_player = input("> ")

current_player = first_player

while pencils > 0:
    print('|' * pencils)
    print(f"{current_player}'s turn:")

    while True:
        take = input("> ")
        if take not in ['1', '2', '3']:
            print("Possible values: '1', '2' or '3'")
            continue
        take = int(take)
        if take > pencils:
            print("Too many pencils were taken")
            continue
        break

    pencils -= take
    if pencils == 0:
        winner = players[1] if current_player == players[0] else players[0]
        print(f"{winner} won!")
        break

    current_player = players[1] if current_player == players[0] else players[0]
import random

def bot_move(pencils):
    if pencils % 4 == 0:
        return random.randint(1, 3)
    else:
        return pencils % 4

names = ["John", "Jack"]
while True:
    pencils = input("How many pencils would you like to use:\n")
    if not pencils.isdigit():
        print("The number of pencils should be numeric")
        continue
    pencils = int(pencils)
    if pencils <= 0:
        print("The number of pencils should be positive")
        continue
    break

while True:
    first = input(f"Who will be the first ({names[0]}, {names[1]}):\n")
    if first not in names:
        print(f"Choose between '{names[0]}' and '{names[1]}'")
        continue
    break

print("|" * pencils)

current = first
while pencils > 0:
    if current == "Jack":  # бот
        take = bot_move(pencils)
        print(f"Jack's turn:")
        print(take)
    else:
        print(f"{current}'s turn:")
        while True:
            take = input()
            if take not in ["1", "2", "3"]:
                print("Possible values: '1', '2' or '3'")
                continue
            take = int(take)
            if take > pencils:
                print("Too many pencils were taken")
                continue
            break
    pencils -= take
    if pencils == 0:
        print(f"{'Jack' if current == 'John' else 'John'} won!")
        break
    print("|" * pencils)
    current = "Jack" if current == "John" else "John"
