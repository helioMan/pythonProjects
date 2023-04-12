import random

enterTheRange = int(input("Enter the range you want to have the number up to: "))
random_random_number = random.randint(0, enterTheRange)
guesses = 0

while True:
    guesses += 1
    guessOfUser = int(input("Go ahead, make a guess: "))
    if guessOfUser == random_random_number:
        print("Well, that is correct!")
        break
    elif guessOfUser > random_random_number:
        print("The guess is above the number!")
    else:
        print("The guess is below the number!")
print(f"You guessed it correctly in {guesses} guesses")
