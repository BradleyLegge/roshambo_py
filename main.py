import random

def get_instructions():
    print("Winning rules of the game ROCK PAPER SCISSORS are:")
    print("Rock vs Paper -> Paper wins")
    print("Rock vs Scissors -> Rock wins")
    print("Paper vs Scissors -> Scissors wins\n")

    print("Enter your choice")
    print("1 - Rock")
    print("2 - Paper")
    print("3 - Scissors")

def get_choice(choice):
    if( choice == 1):
        return "Rock"
    elif( choice == 2):
        return "Paper"
    elif( choice == 3):
        return "Scissors"
    else:
        return "Invalid choice"

def get_computer_choice():
    comp_choice = random.randint(1,3)
    return comp_choice

def get_winner(user, computer):
    if(user == computer):
        return "<== It's a tie! ==>"
    elif (user == "Rock" and computer == "Scissors") or (user == "Paper" and computer == "Rock") or (user == "Scissors" and computer == "Paper"):
        return "<== You win! ==>"
    elif (computer == "Rock" and user == "Scissors") or (computer == "Paper" and user == "Rock") or (computer == "Scissors" and user == "Paper"):
        return "<== Computer wins! ==>"
    
def play_again(answer):
    if(answer.lower() == "y"):
        main()
    elif(answer.lower() =="n"):
        exit
    else:
        print("Invalid input. Please enter 'Y' or 'N'.")
        answer = input("Do you want to play again? (Y/N): ")
        play_again(answer)

def main():
    get_instructions()

    # Update: Would like to move this while loop into its own validation function
    while True: 
        try: 
            user_input = int(input("Enter your choice (1-3): "))
            while 1 < user_input > 3:
                user_input = int(input("Please choose a number between 1 and 3: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 3: ") 

    users_choice = get_choice(user_input)
    print(f"Your choice is: {users_choice}")

    print("Now it's Computer's Turn. . .")
    computer_input = get_computer_choice()
    computer_choice = get_choice(computer_input)
    print(f"Computer choice is: {computer_choice}")

    print(f"{users_choice} vs {computer_choice}")
    print(get_winner(users_choice, computer_choice))
    answer = input("Do you want to play again? (Y/N) ")
    play_again(answer)

if __name__ == "__main__":
    main()