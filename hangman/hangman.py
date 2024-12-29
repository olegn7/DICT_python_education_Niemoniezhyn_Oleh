print("HANGMAN")
print("The game will be available soon.")
print("HANGMAN")
word = "python"
guess = input("Guess the word: > ").strip()

if guess == word:
    print("You survived!")
else:
    print("You lost!")
import random

print("HANGMAN")
words = ['python', 'java', 'javascript', 'php']
word = random.choice(words)
guess = input("Guess the word: > ").strip()

if guess == word:
    print("You survived!")
else:
    print("You lost!")
import random

print("HANGMAN")
words = ['python', 'java', 'javascript', 'php']
word = random.choice(words)
hint = word[:3] + '-' * (len(word) - 3)
print(f"Guess the word {hint}: ", end="")
guess = input("> ").strip()

if guess == word:
    print("You survived!")
else:
    print("You lost!")
import random

print("HANGMAN")
words = ['python', 'java', 'javascript', 'php']
word = random.choice(words)
hidden_word = ['-' for _ in word]
attempts = 8

while attempts > 0:
    print("\n" + ''.join(hidden_word))
    letter = input("Input a letter: > ").strip()

    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                hidden_word[i] = letter
        if '-' not in hidden_word:
            print(f"You guessed the word {word}!")
            print("You survived!")
            break
    else:
        print("That letter doesn't appear in the word")
        attempts -= 1

if '-' in hidden_word:
    print("You lost!")
import random

def play_hangman():
    words = ['python', 'java', 'javascript', 'php']
    word = random.choice(words)
    hidden_word = ['-' for _ in word]
    attempts = 8
    guessed_letters = set()

    print("HANGMAN")

    while attempts > 0:
        print("\n" + ''.join(hidden_word))
        letter = input("Input a letter: > ").strip()


        if letter in guessed_letters:
            print("No improvements")
            attempts -= 1
            continue

        guessed_letters.add(letter)


        if letter in word:
            for i in range(len(word)):
                if word[i] == letter:
                    hidden_word[i] = letter
            if '-' not in hidden_word:
                print(f"You guessed the word {word}!")
                print("You survived!")
                break
        else:
            print("That letter doesn't appear in the word")
            attempts -= 1

    if '-' in hidden_word:
        print("You lost!")
import random

def play_hangman():
    words = ['python', 'java', 'javascript', 'php']
    word = random.choice(words)
    hidden_word = ['-' for _ in word]
    attempts = 8
    guessed_letters = set()

    print("HANGMAN")

    while attempts > 0:
        print("\n" + ''.join(hidden_word))
        letter = input("Input a letter: > ").strip()

        # Проверка длины ввода
        if len(letter) != 1:
            print("You should input a single letter")
            continue

        # Проверка на строчную букву
        if not letter.islower():
            print("Please enter a lowercase English letter")
            continue

        # Проверка на повторный ввод
        if letter in guessed_letters:
            print("You've already guessed this letter")
            continue

        guessed_letters.add(letter)

        # Проверяем, есть ли буква в слове
        if letter in word:
            for i in range(len(word)):
                if word[i] == letter:
                    hidden_word[i] = letter
            if '-' not in hidden_word:
                print(f"You guessed the word {word}!")
                print("You survived!")
                break
        else:
            print("That letter doesn't appear in the word")
            attempts -= 1

    if '-' in hidden_word:
        print("You lost!")
import random

def play_hangman():
    words = ['python', 'java', 'javascript', 'php']
    word = random.choice(words)
    hidden_word = ['-' for _ in word]
    attempts = 8
    guessed_letters = set()

    print("HANGMAN")

    while attempts > 0:
        print("\n" + ''.join(hidden_word))
        letter = input("Input a letter: > ").strip()

        if len(letter) != 1:
            print("You should input a single letter")
            continue
        if not letter.islower():
            print("Please enter a lowercase English letter")
            continue
        if letter in guessed_letters:
            print("You've already guessed this letter")
            continue

        guessed_letters.add(letter)

        if letter in word:
            for i in range(len(word)):
                if word[i] == letter:
                    hidden_word[i] = letter
            if '-' not in hidden_word:
                print(f"You guessed the word {word}!")
                print("You survived!")
                break
        else:
            print("That letter doesn't appear in the word")
            attempts -= 1

    if '-' in hidden_word:
        print("You lost!")


while True:
    print("\nHANGMAN")
    choice = input('Type "play" to play the game, "exit" to quit: > ').strip()
    if choice == "play":
        play_hangman()
    elif choice == "exit":
        break
    else:
        print('Invalid choice. Please type "play" or "exit".')
