def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_win(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def is_board_full(board):
    return all(cell != " " for row in board for cell in row)


def get_empty_cells(board):
    empty_cells = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                empty_cells.append((row, col))
    return empty_cells


def minimax(board, depth, is_maximizing):
    scores = {"X": -1, "O": 1, "tie": 0}

    if check_win(board, "X"):
        return scores["X"]
    if check_win(board, "O"):
        return scores["O"]
    if is_board_full(board):
        return scores["tie"]

    if is_maximizing:
        best_score = -float("inf")
        for row, col in get_empty_cells(board):
            board[row][col] = "O"
            score = minimax(board, depth + 1, False)
            board[row][col] = " "
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for row, col in get_empty_cells(board):
            board[row][col] = "X"
            score = minimax(board, depth + 1, True)
            board[row][col] = " "
            best_score = min(score, best_score)
    return best_score


def best_move(board):
    best_score = -float("inf")
    best_move = None
    for row, col in get_empty_cells(board):
        board[row][col] = "O"
        score = minimax(board, 0, False)
        board[row][col] = " "
        if score > best_score:
            best_score = score
            best_move = (row, col)
    return best_move


def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Hrestyky Nolyky!")

    while True:
        print_board(board)
        try:
            row = int(input("Enter row (0, 1, 2): "))
            col = int(input("Enter column (0, 1, 2): "))

            if row > 2 or col > 2:
                raise TypeError
        except (TypeError, ValueError):
            print("Enter valid values for row and column.")
            continue

        if board[row][col] == " ":
            board[row][col] = "X"
        else:
            print("That cell is already occupied. Try again.")
            continue

        if check_win(board, "X"):
            print_board(board)
            print("Player X wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        print("Computer is thinking...")
        computer_move = best_move(board)
        board[computer_move[0]][computer_move[1]] = "O"

        if check_win(board, "O"):
            print_board(board)
            print("Computer wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break


if __name__ == "__main__":
    play_game()
