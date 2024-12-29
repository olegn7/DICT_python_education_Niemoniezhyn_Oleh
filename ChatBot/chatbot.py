print("Hello! My Name is KAN_bot. ")
print("I was created in 2024. ")
print(" Please, remind me your name. ")
user_name = input("> Oleh")
print(f"What a great name you have, {user_name}! ")
print("Let me guess your age.")
print("Enter remainders of dividing your age by 3, 5 and 7.")
print("> 0")
print("> 3")
print("> 4")
rem3 = 0
rem5 = 3
rem7 = 4
age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105
print(f"Your age is {age}; that's a good time to start programming!")
print("Now I will prove to you that I can count to any number you want.")
print("> 4")
num = 4
for i in range(num + 1):
    print(f"{i} !")
print("Completed, have a nice day!")
print("Let's test your programming knowledge.")
print("What is a line called?")
print("1. Character set")
print("2. Set of numbers")
print("3. Expression")
print("4. Code snippet")
while True:
    answer = int(input("> "))
    if answer == 4:
        print("Congratulations, have a nice day!")
        break
    else:
        print("Please, try again.")
