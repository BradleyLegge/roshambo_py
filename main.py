import random

def get_user_input(message):
    while True:
        try:
            poop = int(input(message))
        except ValueError:
            print("Not a valid number! Try again!")
            continue
        else:
            return poop

def get_user_choice(choice):
    match choice:
        case 1:
            return "Rock"
        case 2:
            return "Paper"
        case 3:
            return "Scissors"
        case _:
            "Error"

def get_computer_choice(users_input):
    comp_choice = random.randint(1,3)
    print(users_input)
    print(comp_choice)
    while(users_input == comp_choice):
        comp_choice = random.randint(1,3)
        print(comp_choice)
        

        

def main():
    print("Winning rules of the game ROCK PAPER SCISSORS are:")
    print("Rock vs Paper -> Paper wins")
    print("Rock vs Scissors -> Rock wins")
    print("Paper vs Scissors -> Scissors wins\n")

    print("Enter your choice")
    print("1 - Rock")
    print("2 - Paper")
    print("3 - Scissors")
    users_input = get_user_input("Enter your choice: ")
    users_choice = str(get_user_choice(users_input))
    print(f"Your choice is: {users_choice}")
    print("Now it's Computer's Turn. . .")
    computer_choice = get_computer_choice(users_choice)
    print(f"Computer choice is: {computer_choice}")
    # print(f"{user_choice} vs {computer_choice}")

if __name__ == "__main__":
    main()