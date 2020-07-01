import sys, random, time

print("*** ROCK, PAPER, SCISSORS ***")
print(r'''
Rules: 1. ROCK wins over SCISSORS
       2. SCISSORS wins over PAPER
       3. PAPER wins over ROCK
''')

wins ,losses ,ties = 0, 0, 0 

while True: # main game loop
    print("You have {} win(s) {} tie(s) {} loss(es)".format(wins, ties, losses))

    # user input loop
    while True:
        print("Input your choice: rock (r), paper (p), scissors (s), quit (q)")
        player_choice = input()
        if player_choice.isalpha():
            player_choice = player_choice.lower()
            if player_choice == 'q':
                sys.exit()
            elif player_choice == 'r' or player_choice == 'p' or player_choice == 's':
                break
        else:
            print("Please input a valid choice from these: 'r', 'p', 's' or 'q'")

    # print player's choice
    if player_choice == 'r':
        print("ROCK versus...")
        time.sleep(1)
    elif player_choice == 'p':
        print("PAPER versus...")
        time.sleep(1)
    elif player_choice == 's':
        print("SCISSORS versus...")
        time.sleep(1)

    computer_pick = random.choice(['r','p','s']) 
    # print computer's choice
    if computer_pick == 'r':
        print("ROCK")
        time.sleep(1)
    elif computer_pick == 'p':
        print("PAPER")
        time.sleep(1)
    elif computer_pick == 's':
        print("SCISSORS")
        time.sleep(1)

    # the game rules implementation
    if player_choice == computer_pick:
        print("It's a tie")
        ties += 1
    elif (player_choice == 'r' and computer_pick == 's')\
    or (player_choice == 'p' and computer_pick == 'r')\
    or (player_choice == 's' and computer_pick == 'p'):
        print("You win!!")
        wins += 1
    elif (player_choice == 's' and computer_pick == 'r')\
    or (player_choice == 'r' and computer_pick == 'p')\
    or (player_choice == 'p' and computer_pick == 's'):
        print("You loose!!")
        losses += 1
