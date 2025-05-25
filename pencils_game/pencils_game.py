import random

def bot_move(pencils):
    if pencils % 4 == 0:
        return random.randint(1, 3)
    else:
        return pencils % 4

players = ["John", "Jack"]

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
    first = input(f"Who will be the first ({players[0]}, {players[1]}):\n")
    if first not in players:
        print(f"Choose between '{players[0]}' and '{players[1]}'")
        continue
    break

print("|" * pencils)

current = first
while pencils > 0:
    if current == "Jack":
        take = bot_move(pencils)
        print("Jack's turn:")
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
