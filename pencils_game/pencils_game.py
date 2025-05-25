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
