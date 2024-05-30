import os

# Dictionary with board fields
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
    winning_combinations = [
        (1, 2, 3), (4, 5, 6), (7, 8, 9),
        (1, 4, 7), (2, 5, 8), (3, 6, 9),
        (1, 5, 9), (3, 5, 7)
    ]
    for combo in winning_combinations:
        if fields[combo[0]] == fields[combo[1]] == fields[combo[2]]:
            return True
    return False


def check_draw(fields):
    return all(fields[key] in {'X', 'O'} for key in fields)


def minimax(fields, depth, is_maximizing):
    if check_win(fields):
        return 1 if not is_maximizing else -1
    if check_draw(fields):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for key in fields:
            if fields[key] not in {'X', 'O'}:
                original = fields[key]
                fields[key] = 'O'
                score = minimax(fields, depth + 1, False)
                fields[key] = original
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for key in fields:
            if fields[key] not in {'X', 'O'}:
                original = fields[key]
                fields[key] = 'X'
                score = minimax(fields, depth + 1, True)
                fields[key] = original
                best_score = min(score, best_score)
        return best_score


def find_best_move(fields):
    best_move = None
    best_score = -float('inf')
    for key in fields:
        if fields[key] not in {'X', 'O'}:
            original = fields[key]
            fields[key] = 'O'
            score = minimax(fields, 0, False)
            fields[key] = original
            if score > best_score:
                best_score = score
                best_move = key
    return best_move


# Game loop
while game_on:
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Welcome to Tic Tac Toe Game')
    draw_board(fields)
    if turn % 2 != 0:
        player_choice = find_best_move(fields)  # AI's turn
        if player_choice is not None:
            fields[player_choice] = 'O'
            turn += 1
    else:
        print("Player 1: Pick a spot or press q to quit.")
        player_choice = input('')
        if player_choice == 'q':
            game_on = False
        elif str.isdigit(player_choice) and int(player_choice) in fields:
            if fields[int(player_choice)] not in {"X", "O"}:
                fields[int(player_choice)] = 'X'
                turn += 1

    if check_win(fields):
        game_on, win = False, True
    if turn > 8:
        game_on = False

os.system('cls' if os.name == 'nt' else 'clear')
draw_board(fields)

if win:
    if check_turn(turn) == 'X':
        print("Player 1 Wins!")
    else:
        print("Player 2 (AI) Wins!")
else:
    print("No Winner")

print("Thanks for playing!")
