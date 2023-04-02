import random
import string
import time

import art
from clear import clear_terminal

LOGO = art.logo
letters = list(string.ascii_uppercase)
default_lets = ["X", "O"]
player_dict = {}


def clear_print_logo():
    clear_terminal()
    print(LOGO)


def get_game_mode():
    error_msg = "Invalid entry. Please type 1 or 2 to proceed"
    input_msg = "SELECT A MODE FROM THE MODES BELOW TO PROCEED BY TYPING 1 OR 2\n1. Single player\n2. Multi player\n"
    mode = input(input_msg)

    while not mode.isdigit():
        print(error_msg)
        mode = input(input_msg)
    mode = int(mode)
    while mode not in range(1, 3):
        print(error_msg)
        mode = int(input(input_msg))
    if mode == 1:
        return False
    else:
        return True


def print_board():
    sample_board = [1, 2, 3,
                    # this is just a show board to guide the players on how to insert their letters in the matrix(board)
                    4, 5, 6,
                    7, 8, 9,
                    ]

    print("Below, is the board,type in the corresponding number to input your letter in the position")

    print(f"{sample_board[0]} | {sample_board[1]} | {sample_board[2]}")
    print(f"{sample_board[3]} | {sample_board[4]} | {sample_board[5]}")
    print(f"{sample_board[6]} | {sample_board[7]} | {sample_board[8]}")


def single_player(one_player):
    if not one_player:
        global player_dict

        computer_name = "Computer"
        player_name = input("Please,type in your name or press enter to use default name: ").capitalize()
        if player_name == "":
            player_name = "Player1"
        letter = input(
            f"{player_name}, choose a letter between X and O or press enter to receive a letter automatically").upper()

        while letter not in default_lets and not letter == "":
            print("Invalid. Please type a valid letter!")
            letter = input(
                f"{player_name}, a letter between X and O or press enter to receive a letter automatically").upper()

        if letter == "":
            letter = random.choice(default_lets)
            print(f"Your letter is {letter}")
        if letter == "X":
            comp_let = "O"
        else:
            comp_let = "X"
        player_dict = {player_name: letter, computer_name: comp_let}
        return player_dict


def get_players_data():
    """function to get the data of the players,e.g., player names,letter"""
    global player_dict

    for i in range(2):
        name = input(
            f"Player{i + 1},type in your name or press enter to use default name: ").capitalize()
        if name == "":
            # the program gives the players default names
            name = f"Player{i + 1}"
            # the program gives each player default letters to play with
        player_dict[name] = default_lets[i]
        print(f"{name}, your letter is {default_lets[i]}")
        if i == 1:
            time.sleep(1)
    return player_dict


def get_winner(player_data, who_won_last_round, multi_player):
    """this is the main function that actually takes in the player values and determines the winner"""
    winner = None
    game_board = ["_", "_", "_",
                  # Initialize the board the players actually play with,i.e., where their letters are inserted
                  "_", "_", "_",
                  "_", "_", "_",
                  ]
    print_board()

    pass_turn = False
    pos = []
    end_game = False
    comp_plays = "Computer plays the following:"

    if who_won_last_round == "X":
        print("Your letters will be switched")
        for xx in player_data:
            if player_data[xx] == who_won_last_round:
                player_data[xx] = "O"
            else:
                player_data[xx] = "X"
    elif who_won_last_round == "O":
        who_won_last_round = "X"
    while not end_game:
        comp_list = []
        for i in range(1, 10):
            if game_board[i - 1] == "_":
                comp_list.append(i)

        for names in player_data:
            # if the players want to proceed to a next round, the round starts with the loser of the previous game
            if who_won_last_round == player_data[names] or who_won_last_round == '':
                who_won_last_round = ''
                current_player = names  # save the current person who started a new round;if the previous round was a
                # draw, the next round does not start with this player
                if not pass_turn:
                    if multi_player:
                        player_ = input(
                            f"{names} it is your turn: type a number to proceed or type 'N' to pass your turn -->")
                    else:
                        if names != "Computer":
                            player_ = input(
                                f"{names} it is your turn: type a number to proceed or type 'N' to pass your turn -->")
                        else:
                            print(comp_plays)
                            random.shuffle(comp_list)
                            random.shuffle(comp_list)
                            player_ = str(random.choice(comp_list))
                    while player_ in pos:
                        if multi_player:
                            player_ = input(
                                f"{names} the position is filled.Type a different number to proceed or type 'N' to "
                                f"pass your turn -->")
                        else:
                            if names != "Computer":
                                player_ = input(
                                    f"{names} the position is filled.Type a different number to proceed or type 'N' "
                                    f"to pass your turn -->")
                            else:
                                # while player_ in pos:
                                print(comp_plays)
                                random.shuffle(comp_list)
                                random.shuffle(comp_list)
                                player_ = str(random.choice(comp_list))
                    if not player_ == "n":
                        pos.append(player_)
                else:
                    if multi_player:
                        player_ = input(
                            f"{names} ,your opponent passed his turn: type a number to proceed or type 'N' to pass "
                            f"your turn -->")
                    else:
                        if names != "Computer":
                            player_ = input(
                                f"{names}, it is your turn: type a number to proceed or type 'N' to pass your turn -->")
                        else:
                            print(f"You passed your turn,computer will now play")
                            random.shuffle(comp_list)
                            random.shuffle(comp_list)
                            player_ = str(random.choice(comp_list))
                    while player_ in pos:
                        if multi_player:
                            player_ = input(
                                f"{names} the position is filled.Type a different number to proceed or type 'N' to "
                                f"pass your turn -->")
                        else:
                            if names != "Computer":
                                player_ = input(
                                    f"{names} the position is filled.Type a different number to proceed or type 'N' "
                                    f"to pass your turn -->")
                            else:
                                # while player_ in pos:
                                print(comp_plays)
                                random.shuffle(comp_list)
                                random.shuffle(comp_list)
                                player_ = str(random.choice(comp_list))
                    if not player_ == "n":
                        pos.append(player_)
            else:
                continue  # continue to pick the loser from the previous round and start the new round with them
            if player_.isdigit():
                player_ = int(player_)
                pass_turn = False
            elif player_ == "n":
                pass_turn = True
                continue  # continue to the next player since the current player has passed their turn

            game_board[player_ - 1] = player_data[names]
            print(f"\n{game_board[0]} | {game_board[1]} | {game_board[2]}")
            print(f"{game_board[3]} | {game_board[4]} | {game_board[5]}")
            print(f"{game_board[6]} | {game_board[7]} | {game_board[8]}")

            winner_exist = False
            win_lists = [[], [], [], [], [], [], [],
                         [], ]  # lists store positions of wins - horizontal wins,vertical wins and diagonal wins
            val = 0
            while val < 9:
                if val < 3:
                    win_lists[0].append(game_board[val])
                if val in range(3, 6):
                    win_lists[1].append(game_board[val])
                if val in range(6, 9):
                    win_lists[2].append(game_board[val])
                if val in range(0, 7, 3):
                    win_lists[3].append(game_board[val])
                if val in range(1, 8, 3):
                    win_lists[4].append(game_board[val])
                if val in range(2, 10, 3):
                    win_lists[5].append(game_board[val])
                if val in range(0, 9, 4):
                    win_lists[6].append(game_board[val])
                if val in range(2, 7, 2):
                    win_lists[7].append(game_board[val])
                val += 1
            for xos in player_data:
                for lists in range(len(win_lists)):
                    if win_lists[lists].count(player_data[xos]) == 3:
                        winner = player_data[xos]
                        winner_exist = True
                        end_game = True
                    elif not winner_exist and game_board.count("_") == 0:
                        winner_exist = False
                        end_game = True
            if winner_exist:
                return winner, player_data
            elif not winner_exist and end_game:
                # get the actual player who started current round
                who_won_last_round = player_data[current_player]
                return who_won_last_round
            else:
                end_game = False
    clear_print_logo()


def get_scores(the_winner, score_dict):
    """function to Calculate the scores of the players depending on who wins each round """

    if isinstance(the_winner, tuple):
        list(the_winner)
        for names in the_winner[1]:
            if the_winner[0] == the_winner[1][names]:
                print(f"{names} is the winner of this round!")
                score_dict[names] += 1
                return score_dict
    print("This round ends in a draw.")
    return score_dict


def tictactoe_game():
    """function that runs the game"""

    first_run = True  # for every new game, first run is true
    player_data, modes = None, None
    previous_winner = ''  # who won the last round or,if the last round was a draw,who started it
    rounds = 2
    text = "ROUND"
    score = {}  # store the players' names and their respective scores
    games = 0

    while first_run or games in range(1, 4):
        clear_print_logo()
        if first_run:
            modes = get_game_mode()
            if modes:
                player_data = get_players_data()
            else:
                player_data = single_player(modes)
            clear_print_logo()
            print(f"\n\n{text} {1}\n\n")
            for names in player_data:
                score[names] = 0
            first_run = False

        n_list = list(score.keys())
        if games == 1:  # players want to continue current game to a new round
            print(f"\n\n{text} {rounds}\n\n")
            rounds += 1
            print(
                f"Scores Board\n{n_list[0]}: {score[n_list[0]]}            {n_list[1]}: {score[n_list[1]]}\n ")

        true_winner = get_winner(player_data, previous_winner, modes)
        if isinstance(true_winner, tuple):
            previous_winner = true_winner[0]
        else:
            previous_winner = true_winner
        get_scores(true_winner, score)

        games = int(input(
            f"\nContinue game? Press:\n1 to continue to round {rounds}\n2 to end current game\n3 to end current game "
            f"and start new game\n"))
        if games in range(2, 4):  # players want to quit current game
            clear_print_logo()
            print(
                f"Scores Board\n{n_list[0]}: {score[n_list[0]]}            {n_list[1]}: {score[n_list[1]]}\n ")
            sc = []
            for keys in score:
                sc.append(score[keys])
            max_val = max(sc)
            if sc[0] == sc[1]:
                print("The game ends in a draw!")
            else:
                for i in score:
                    if max_val == score[i]:
                        print(f"Congratulations {i},you win the game")
            if games == 3:  # after quitting current game,players want to start new game automatically
                time.sleep(2)
                tictactoe_game()
            else:  # players don't want to start new game
                exit()


tictactoe_game()
