import replit

locations = {
    'A': 0,
    'B': 1,
    'C': 2,
    '1': 0,
    '2': 1,
    '3': 2,
}


# Function to print board
def print_board():
    print(f"  A   B   C \n"
          f"1 {board[0][0]} | {board[0][1]} | {board[0][2]} \n"
          f" -----------\n"
          f"2 {board[1][0]} | {board[1][1]} | {board[1][2]} \n"
          f" -----------\n"
          f"3 {board[2][0]} | {board[2][1]} | {board[2][2]} \n")


# Function to check winner
def check_end():
    global end
    if (
        board[0][0] == board[0][1] == board[0][2] != " " or
        board[1][0] == board[1][1] == board[1][2] != " " or
        board[2][0] == board[2][1] == board[2][2] != " " or
        board[0][0] == board[1][0] == board[2][0] != " " or
        board[0][1] == board[1][1] == board[2][1] != " " or
        board[0][2] == board[1][2] == board[2][2] != " " or
        board[0][0] == board[1][1] == board[2][2] != " " or
        board[0][2] == board[1][1] == board[2][0] != " " or
            len(filled_spaces) == 9):
        end = True


# Player turn
def take_turn(current_player):
    selection = input(f"({current_player}): Choose where to place your turn (eg. A1): ").upper()
    while selection not in ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']:
        selection = input("That was not an accepted input. Choose where to place your turn (eg. A1): ").upper()
    while selection in filled_spaces:
        selection = input("That space is already taken. Choose where to place your turn (eg. A1): ").upper()
    filled_spaces.append(selection)
    selection = list(selection)
    col = locations[selection[0]]
    row = locations[selection[1]]
    board[row][col] = player


# Change player's turn
def change_player(current_player):
    if current_player == starting_player:
        return second_player
    else:
        return starting_player


# Create Board List
board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
end = False

# Choose Starting Player
starting_player = input("Who starts? X or O: ").upper()
while starting_player not in ["X", "O"]:
    starting_player = input("That was not an accepted input. Who starts? X or O: ").upper()

if starting_player == "X":
    second_player = "O"
else:
    second_player = "X"


# Set up game
print_board()
player = second_player
filled_spaces = []
while not end:
    player = change_player(player)
    take_turn(player)
    check_end()
    replit.clear()
    print_board()

# Show winner
if len(filled_spaces) == 9:
    print("It's a draw!")
else:
    print(f"Well done ({player}), you win!")
