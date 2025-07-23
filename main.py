import random

def user_input(message):
    while True:
        try:
            u_input = int(input(message))
        except ValueError:
            print("Not a valid number! Try again!")
            continue
        else:
            return u_input
        

def main():
    print("Winning rules of the game ROCK PAPER SCISSORS are:")
    print("Rock vs Paper -> Paper wins")
    print("Rock vs Scissors -> Rock wins")
    print("Paper vs Scissors -> Scissors wins\n")

    print("Enter your choice")
    print("1 - Rock")
    print("2 - Paper")
    print("3 - Scissors")
    users_input = user_input("Enter your choice: ")
    print(f"Your choice is: {user_choice}")
    print("Now it's Computer's Turn. . .")
    print(f"Computer choice is: {computer_choice}")
    print(f"{user_choice} vs {computer_choice}")

if __name__ == "__main__":
    main()