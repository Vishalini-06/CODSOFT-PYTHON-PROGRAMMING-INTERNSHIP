import random

def determine_winner(player, computer):
    if player == computer:
        return "tie"
    elif (player == 1 and computer == 3) or \
         (player == 3 and computer == 2) or \
         (player == 2 and computer == 1):
        return "user"
    else:
        return "computer"

def stone_paper_scissors():
    print("Welcome to Stone, Paper, Scissors!")
    print("Choices: \n1 = Stone\n2 = Paper\n3 = Scissors\n4 = Exit\n")
    
    while True:
        user_score = 0
        computer_score = 0
        ties = 0
        
        while True:
            try:
                player_choice = int(input("Enter your choice: "))
                
                if player_choice == 4:
                    print("\nThanks for playing!")
                    print("Final Scores:")
                    print(f"You: {user_score}")
                    print(f"Computer: {computer_score}")
                    print(f"Ties: {ties}")
                    break

                if player_choice not in [1, 2, 3]:
                    print("Invalid choice. Please choose 1, 2, 3, or 4.\n")
                    continue

                computer_choice = random.randint(1, 3)
                choices_map = {1: "Stone", 2: "Paper", 3: "Scissors"}
                
                print(f"You chose: {choices_map[player_choice]}")
                print(f"Computer chose: {choices_map[computer_choice]}")

                result = determine_winner(player_choice, computer_choice)
                if result == "tie":
                    print("It's a tie!\n")
                    ties += 1
                elif result == "user":
                    print("You win this round!\n")
                    user_score += 1
                else:
                    print("Computer wins this round!\n")
                    computer_score += 1

            except ValueError:
                print("Invalid input. Please enter a number between 1 and 4.\n")
        
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Goodbye! 👋")
            break
        print("\nRestarting the game...\n")

# Run the game
stone_paper_scissors()
