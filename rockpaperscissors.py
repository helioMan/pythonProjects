import random
numberOfGamesPlayed = 0
numberOfUserWins = 0
matchesDraw = 0
numberOfComputerWins = 0
while True:
    options = ['rock', 'paper', 'scissors']

    computer_choice = random.choice(options)

    user_choice = input(
        "Choose rock, paper, or scissors, or press q to quit the game: ")

    if user_choice == 'q':
        break
    elif user_choice not in options:
        print("Wrong input, chose rock, paper and scissors.")
        continue

    if user_choice == computer_choice:
        print("It is a tie!")
        matchesDraw += 1
        numberOfGamesPlayed += 1
    elif user_choice == 'rock' and computer_choice == 'scissors':
        print("You win!")
        numberOfUserWins += 1
        numberOfGamesPlayed += 1
    elif user_choice == 'paper' and computer_choice == 'rock':
        print("You win!")
        numberOfUserWins += 1
        numberOfGamesPlayed += 1
    elif user_choice == 'scissors' and computer_choice == 'paper':
        print("You win!")
        numberOfUserWins += 1
        numberOfGamesPlayed += 1
    else:
        print("Computer wins")
        numberOfComputerWins += 1
        numberOfGamesPlayed += 1
    # display the result
    print("Computer choice", computer_choice)
    print("Number of games played", numberOfGamesPlayed)
    print(f"The user won {numberOfUserWins} matches")
    print(f"The computer won {numberOfComputerWins} matches")
    print(f"Games tied {matchesDraw}")
    print(f"Games tied percentage is {round((matchesDraw/numberOfGamesPlayed)*100,3)}")
    print(f"User win percentage {round((numberOfUserWins/numberOfGamesPlayed)*100,3)} 100%")
    print(f"Computer win percentage {round((numberOfComputerWins/numberOfGamesPlayed)*100,3)} 100%")
    play_again_game = input("Play again? (y/n)")
    if play_again_game != 'y':
        break
