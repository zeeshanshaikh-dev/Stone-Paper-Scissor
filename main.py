import random


# Store the possible choices and their corresponding values.
choice_dict = {
    "stone": 1,
    "paper": -1,
    "scissor": 0
}

# Convert the numerical values back into choice names.
reverse_dict = {
    1: "stone",
    -1: "paper",
    0: "scissor"
}


# Keep the game running until the player chooses to stop.
while True:

    # Randomly choose a value for the computer.
    computer = random.choice([-1, 0, 1])

    # Ask the player for their choice and convert it to lowercase.
    youstr = input("\nEnter your choice (stone/paper/scissor): ").lower()

    # Check whether the player's choice is valid.
    if youstr not in choice_dict:
        print("Invalid choice. Please enter stone, paper, or scissor.")
        continue

    # Convert the player's choice into its numerical value.
    you = choice_dict[youstr]

    # Display both choices.
    print(f"You Chose: {reverse_dict[you]}")
    print(f"Computer Chose: {reverse_dict[computer]}")

    # Check if both choices are the same.
    if computer == you:
        print("It's a Draw!")

    # Determine whether the player has won.
    elif computer - you == -1 or computer - you == 2:
        print("You Win!")

    # Otherwise, the computer wins.
    else:
        print("You Lose!")

    # Ask whether the player wants to play another round.
    play_again = input("\nPlay again? (yes/no): ").lower()

    # End the game if the player doesn't want to continue.
    if play_again != "yes":
        print("Thanks for playing!")
        break
