# A multiplayer rock, paper, scissors console game,computer plays against human
# computer chooses randomly from rock, paper, scissors
# human chooses from rock, paper, scissors
# player should choose one of the three options nd should be warned if they enter an invalid option
# At each round, the player must enter one of the options in the list and be informed if they won, lost, or tied with the opponent
# By the end of each round, the player can choose whether to play again or quit the game
# Display the player's score at the end of the game
# The game must handle user inputs, putting them in lowercase and informing the user if the option is invalid

import random

# function to get the user's choice
def get_user_choice():
    user_choice = input("Enter your choice (rock/paper/scissors): ")
    return user_choice


# function to get the computer's choice
def get_computer_choice():
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    return computer_choice



# function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif user_choice == 'rock':
        if computer_choice == 'paper':
            return "You lose!"
        else:
            return "You win!"
    elif user_choice == 'paper':
        if computer_choice == 'scissors':
            return "You lose!"
        else:
            return "You win!"
    elif user_choice == 'scissors':
        if computer_choice == 'rock':
            return "You lose!"
        else:
            return "You win!"
    else:
        return "Invalid input!"
    
# function to start the game
def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"You chose {user_choice}, computer chose {computer_choice}")
    print(determine_winner(user_choice, computer_choice))
    play_again = input("Play again? (y/n): ")
    if play_again.lower() == 'y':
        play_game()
    else:
        # print the final score, informing number of wins and rounds
        print("Goodbye!")

# start the game
play_game()