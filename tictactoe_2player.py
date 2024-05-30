import os

# dictionary with board fields
fields = {
    1: '1',
    2: '2',
    3: '3',
    4: '4',
    5: '5',
    6: '6',
    7: '7',
    8: '8',
    9: '9',
}

# Variables
turn = 0
prev_turn = -1
game_on = True
win = False


# Game functions
def draw_board(fields):
    print(f"|{fields[1]}|{fields[2]}|{fields[3]}|\n"
          f"|{fields[4]}|{fields[5]}|{fields[6]}|\n"
          f"|{fields[7]}|{fields[8]}|{fields[9]}|")


def check_turn(turn):
    if turn % 2 == 0:
        return 'O'
    else:
        return 'X'


def check_win(fields):
    if (fields[1] == fields[2] == fields[3]) \
            or (fields[4] == fields[5] == fields[6]) \
            or (fields[7] == fields[8] == fields[8]):
        return True

    elif (fields[1] == fields[4] == fields[7]) \
            or (fields[2] == fields[5] == fields[8]) \
            or (fields[3] == fields[6] == fields[9]):
        return True

    elif (fields[1] == fields[5] == fields[9]) \
            or (fields[3] == fields[5] == fields[7]):
        return True

    else:
        return False


# Game loop
while game_on:
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Welcome to Tic Tac Toe Game')
    draw_board(fields)
    if prev_turn == turn:
        print("You did an invalid entry, please select another field.")
    print("Player " + str((turn % 2) + 1) + ": Pick a spot or press q to quit.")
    player_choice = input('')
    if player_choice == 'q':
        game_on = False
    elif str.isdigit(player_choice) and int(player_choice) in fields:
        if not fields[int(player_choice)] in {"X", "O"}:
            turn += 1
            fields[int(player_choice)] = check_turn(turn)

    if check_win(fields): game_on, win = False, True
    if turn > 8: game_on = False

os.system('cls' if os.name == 'nt' else 'clear')
draw_board(fields)

if win:
    if check_turn(turn) == 'X':
        print("Player 1 Wins!")
    else:
        print("Player 2 Wins!")
else:
    print("No Winner")

print("Thanks for playing!")
