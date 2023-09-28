# Function to print Tic Tac Teo Board

def print_tic_t_t(values):
    print("\n")
    print("\t    |    |")
    print("\t  {}  |  {}  |  {}".format(values[0],values[1],values[2]))
    print('\t____|____|____')

    print("\t    |    |")
    print("\t  {}  |  {}  |  {}".format(values[3], values[4], values[5]))
    print('\t____|____|____')

    print("\t    |    |")
    print("\t  {}  |  {}  |  {}".format(values[6], values[7], values[8]))
    print('\t    |    |   ')
    print("\n")

# Function to print the score board for the game

def print_scoreboard(score_board):
    print("\t-----------------------------------")
    print("\t    SCOREBOARD FOR TIC TACT TOE    ")
    print("\t-----------------------------------")

    players = list(score_board.keys())
    print("\t  ",players[0], "\t  ", score_board[players[0]])
    print("\t  ",players[1], "\t  ", score_board[players[2]])

    print("\t---------------------------------\n")

# Function to check if any player has won the game

def check_winner(player_position, current_player):
# All possible winning combinations for the players
soln = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]

# Loop to check if any winning combination satisfies in the iteration
for x in soln:
    if all(y in player_position[current_player] for y in x):
# Return True if any winning combination satisfies in the iteration
    return True

# Return False if the above combination is not satisfied
return False;

