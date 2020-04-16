import sys, random

print("*** ROCK, PAPER, SCISSORS ***")

wins = 0 
losses = 0
ties = 0 # variables to keep track of wins, losses and ties for player

while True: # main game loop
    print("You have {} wins {} ties {} losses".format(wins, losses, ties))
    while True:
        print("Your choice: rock (r), paper (p), scissors (s), quit (q)")
        player_choice = input()
        if player_choice == 'q':
            sys.exit()
        elif player_choice == 'r' or player_choice == 'p' or player_choice == 's':
            break
        else:
            print("Please input a valid choice: 'r', 'p', 's' or 'q'")

    # print player's choice
    if player_choice == 'r':
        print("ROCK versus...")
    elif player_choice == 'p':
        print("PAPER versus...")
    elif player_choice == 's':
        print("SCISSORS versus...")

    computer_pick = random.choice(['r','p','s']) # let the computer make a random pick
    # print computer's choice
    if computer_pick == 'r':
        print("ROCK")
    elif computer_pick == 'p':
        print("PAPER")
    elif computer_pick == 's':
        print("SCISSORS")

    # compare player and computer picks
    if player_choice == computer_pick:
        print("It's a tie")
        ties += 1
    elif (player_choice == 'r' and computer_pick == 's') or (player_choice == 'p' and computer_pick == 'r') or (player_choice == 's' and computer_pick == 'p'):
        print("You win!!")
        wins += 1
    elif (player_choice == 's' and computer_pick == 'r') or (player_choice == 'r' and computer_pick == 'p') or (player_choice == 'p' and computer_pick == 's'):
        print("You loose!!")
        losses += 1
