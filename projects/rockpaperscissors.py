import random

options = ["rock", "paper", "scissors"]


def rps():
    user_choice = None
    while user_choice != options:
        computer_choice = random.choice(options)
        user_choice = input(f"Please choose one of these options {options}: \n").lower()

        if computer_choice == "rock" and user_choice == "rock":
            print("The computer chose rock, It's a draw!")
            replay()
            break
        elif computer_choice == "rock" and user_choice == "scissors":
            print("The computer chose rock, You have lost!")
            replay()
            break
        elif computer_choice == "rock" and user_choice == "paper":
            print("The computer chose rock, You have won!")
            replay()
            break
        elif computer_choice == "paper" and user_choice == "paper":
            print("The computer chose paper, It's a draw!")
            replay()
            break
        elif computer_choice == "paper" and user_choice == "scissors":
            print("The computer chose paper, You have lost!")
            replay()
            break
        elif computer_choice == "paper" and user_choice == "rock":
            print("The computer chose paper, You have won!")
            replay()
            break
        elif computer_choice == "scissors" and user_choice == "scissors":
            print("The computer chose scissors, It's a draw!")
            replay()
            break
        elif computer_choice == "scissors" and user_choice == "rock":
            print("The computer chose scissors, You have lost!")
            replay()
            break
        elif computer_choice == "scissors" and user_choice == "paper":
            print("The computer chose scissors, You have won!")
            replay()
            break
        else:
            print(f"That is not an option, please choose from on of these {options}!")
            continue


def replay():
    again = None
    while again != "yes" or "no":
        again = input("\nWould you like to play again?\n").lower()
        if again == "yes":
            print("Okay, lets plays again.\n")
            rps()
            break
        elif again == "no":
            print("\nYou have decided not to play again, Goodbye.")
            exit()
        else:
            print("\nThat is not an option, please choose 'yes' or 'no'!")
            continue


rps()

replay()


