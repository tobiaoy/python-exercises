import random

player_wins = 0
computer_wins = 0
play = True

# function to determine the user's choice
def player_choice(user_choice):
    #user_choice = str()
    #user_choice = input("Enter Rock, Paper or Scissors: ")

    if user_choice in ["Rock", "rock", "R", "r"]:
        user_choice = "r"
    elif user_choice in ["Paper", "paper", "P", "p"]:
        user_choice = "p"
    elif user_choice in ["Scissors", "scissors", "S", "s"]:
        user_choice = "s"
    else:
        print("That wasn't an option. Try again later.")
    return user_choice

# function to determine computer's choice
def computer_choice(pc_choice):

    if pc_choice == 1:
        pc_choice = "r"
    elif pc_choice == 2:
        pc_choice = "p"
    else:
        pc_choice = "s"

    return pc_choice

# Repeat games -> While loop
while play == True:
    print("")

    player = input("Enter value:")
    p_choice = player_choice(player)
    com = random.randint(1, 3)
    c_choice = computer_choice(com)

    print("")

    # Tied scenario
    if player_choice == computer_choice:
        print("You chose " + p_choice + " and computer chose " + c_choice + ". It was a tie.")

    # Losing scenarios
    if p_choice == "r" and c_choice == "p":
        print("You chose rock and computer chose paper. You lose.")
        computer_wins += 1

    if p_choice == "p" and c_choice == "s":
        print("You chose paper and computer chose scissors. You lose.")
        computer_wins += 1

    if p_choice == "s" and c_choice == "r":
        print("You chose scissors and computer chose rock. You lose.")
        computer_wins += 1

    # Winning scenarios
    if p_choice == "r" and c_choice == "s":
        print("You chose rock and computer chose scissors. You win.")
        player_wins += 1

    if p_choice == "p" and c_choice == "r":
        print("You chose paper and computer chose rock. You win.")
        player_wins += 1

    if p_choice == "s" and c_choice == "p":
        print("You chose scissors and computer chose paper. You win.")
        player_wins += 1

    # Print results
    print("")
    print("Player: " + str(player_wins))
    print("Computer: " + str(computer_wins))

    replay = input("Do you want to play again? ")
    if replay in ["Yes", "yes", "Y", "y", "YES"]:
        play = True
    elif replay in ["No", "no", "N", "n", "NO"]:
        play = False
    else:
        play = False