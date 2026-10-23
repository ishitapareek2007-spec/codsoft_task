board = [" " for _ in range(9)]

def print_board():
    print()
    for i in range(0, 9, 3):
        print(board[i], "|", board[i+1], "|", board[i+2])
        if i < 6:
            print("--+---+--")
    print()

def winner(player):
    win = [(0,1,2),(3,4,8),(6,7,8),
           (0,3,6),(1,4,7),(2,5,8),
           (0,4,8),(2,4,6)]

    for a, b, c in win:
        if board[a] == board[b] == board[c] == player:
            return True
    return False

def draw():
    return " " not in board

# Minimax
def minimax(is_ai):

    if winner("O"):
        return 1

    if winner("X"):
        return -1

    if draw():
        return 0

    if is_ai:
        best = -100

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best = max(best, score)

        return best

    else:
        best = 100

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best = min(best, score)

        return best

def ai_move():

    best_score = -100
    move = -1

    for i in range(9):

        if board[i] == " ":

            board[i] = "O"

            score = minimax(False)

            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    board[move] = "O"

print("Positions:")
print("1 | 2 | 3")
print("--+---+--")
print("4 | 5 | 6")
print("--+---+--")
print("7 | 8 | 9")

while True:

    print_board()

    move = int(input("Enter position (1-9): ")) - 1

    if move < 0 or move > 8 or board[move] != " ":
        print("Invalid Move!")
        continue

    board[move] = "X"

    if winner("X"):
        print_board()
        print(" You Win!")
        break

    if draw():
        print_board()
        print("Draw!")
        break

    print("AI is thinking...")

    ai_move()

    if winner("O"):
        print_board()
        print("AI Wins!")
        break

    if draw():
        print_board()
        print("Draw!")
        break
