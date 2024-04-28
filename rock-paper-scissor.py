import random

# Function to get user's choice
def get_user_choice():
    choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    return choice

# Function to generate computer's choice
def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

# Main function to play the game
def main():
    print("Welcome to Rock-Paper-Scissors game!")

    play_again = 'y'
    user_score = 0
    computer_score = 0

    while play_again.lower() == 'y':
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print("You chose:", user_choice)
        print("Computer chose:", computer_choice)

        result = determine_winner(user_choice, computer_choice)
        print(result)

        # Update scores
        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1

        # Display scores
        print("Scores:")
        print("You:", user_score)
        print("Computer:", computer_score)

        play_again = input("Do you want to play again? (y/n): ")

    print("Thanks for playing!")

if __name__ == "__main__":
    main()
