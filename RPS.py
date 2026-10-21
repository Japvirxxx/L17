import random

while True:
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please try again.")
        continue

    computer_choice = random.choice(["rock", "paper", "scissors"])
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    
    elif user_choice == "rock":
        if computer_choice == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")  
    elif user_choice == "paper":
        if computer_choice == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cut paper! You lose.")
    elif user_choice == "scissors":
        if computer_choice == "paper":
            print("Scissors cut paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break