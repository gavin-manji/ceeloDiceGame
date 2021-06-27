import random

# STUDENT ID: THGMI202
# NAME      : Thawalampitiya Mudiyanselage Gavin Manjitha
# Assignment: Ceelo-Dice Game
# Subject   : CSP1150A – Programming Principles
# Semester  :
# Class     : 2 (Wednesday class - Ms. SIVASUBARAMANIAM, Priyatharshini)

""" This is Cee-lo Dice Game.
    Prompt to Enter the number of players going to play the game and maximum number of players should be 4.
    There are 3 dices used in this game.
    Each Player can select the number of rounds to re-roll the dice, after the first roll of dice. 
    Scores are added like this --> 10 points for each dice you match with the random draw of dice by the CPU 
    So, if you match all three dices with the three dices of the Computer randomly drawn,
    then you will get total of 30 points
    NOTE: If 2 or more players get the same score first player who receives the highest score
    is declared ast the highest of them. (Therefore, there will always be a winner)"""


def display_rules():
    
    print("\n")
    print("\t  \t ! WELCOME TO THE CEE-LO DICE GAME !")
    print("\n")

    print("\t ------- RULES OF THE GAME -------")
    print("This is Cee-lo Dice Game.")
    print("Enter the number of players going to play the game when prompted, "
          "and maximum number of players should be 4")
    print("There are 3 dices used in this game.")
    print("Each Player can select the number of rounds to re-roll the dice, after the first roll of dice. ")
    print(
        "Scores are added like this --> 10 points for each dice you match with the random draw of dice by the CPU ")
    print("So, if you match all three dices with the three dices of the "
          "Computer randomly drawn, then you will get total of 30 points")

    print("Winner is the highest scorer of points")

    print("SPECIAL NOTE : If 2 or more players get the same score, first player who receives the "
          "highest score is declared as the highest of them.\n(Therefore, there will always be a winner)")

    print("ARE YOU READY to start the game ???")

    input("\nPress ENTER to start the Game...")
    print()


def game(computer_numbers, player):
    dice_1_result = random.randint(1, 6)
    dice_2_result = random.randint(1, 6)
    dice_3_result = random.randint(1, 6)

    print(
        f"The Result of player{player + 1} is : {dice_1_result, dice_2_result, dice_3_result} ")
    # Score calculation process
    score = 0

    if dice_1_result == computer_numbers[0] and dice_2_result == \
            computer_numbers[1] and dice_3_result == computer_numbers[2]:
        score = score + 30
        print(f"The score is: {score}")
    elif dice_1_result == computer_numbers[0] and dice_2_result == \
            computer_numbers[1]:
        score = score + 20
        print(f"The score is: {score}")
    elif dice_1_result == computer_numbers[0] and dice_3_result == \
            computer_numbers[2]:
        score = score + 20
        print(f"The score is: {score}")
    elif dice_2_result == computer_numbers[1] and dice_3_result == \
            computer_numbers[2]:
        score = score + 20
        print(f"The score is: {score}")
    elif dice_1_result == computer_numbers[0] or dice_2_result == \
            computer_numbers[1] or dice_3_result == computer_numbers[2]:
        score = score + 10
        print(f"The score is: {score}")
    else:
        print(f"The score is: {score}")

    return score


def dice_game():
    try:
        play_again = 'y'
        display_rules()

        while play_again == 'y':

            random_number_1 = random.randint(1, 6)
            random_number_2 = random.randint(1, 6)
            random_number_3 = random.randint(1, 6)

            computer_numbers = [random_number_1, random_number_2,
                                random_number_3]

            print(f"Random outputs to be matched by the players:"
                  f" {random_number_1, random_number_2, random_number_3} \n")
            # Check the number of players
            players = int(input("How many players are playing the game:"))

            if players > 4:
                print("\nError ! ",end = '')
                print("LIMIT THE MAXIMUM NUMBER OF PLAYERS TO 4..."
                      "Therefore enter a number between 1 and 4 \t ")
                raise ValueError()

            all_players_score = []

            for player in range(0, players):
                print('\n')
                print(">>> Player", player + 1)
                player_total_score = 0


                round_score = game(computer_numbers, player)
                player_total_score += round_score

                # Asking the user whether to re-roll or not ?
                re_roll = (input(
                    "\nDO YOU WANT TO RE-ROLL ???(Enter 'y' or 'Y' to re-roll):")).lower()
                if re_roll == 'y':
                    rounds = int(
                        input("How many rounds you want to roll the dice:"))

                    for x in range(0, rounds):
                        round_score = game(computer_numbers, player)
                        player_total_score += round_score

                all_players_score.append(player_total_score)

            print("\nPlayer scores are (respectively) : ", all_players_score)
            # Winner display
            winning_player = all_players_score.index(max(all_players_score)) + 1

            print("\n-------THE WINNER-------")
            print("Congratulations ! The winning player is ' Player",winning_player,"'")

            print('\n')
            print(" \t \t THANK YOU FOR PLAYING......    PLAY AGAIN !")
            print(
                '- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ')
            play_again = (input(
                "DO YOU WANT TO PLAY AGAIN ???(Enter 'y' or 'Y' to play again):")).lower()
            print('\n')

    except ValueError:
        print(
            "Please Enter an Integer value... Don't enter any other characters \n")
        dice_game()
    except:
        print("Error occurred... Please Enter properly \n")
        dice_game()

        
dice_game()
