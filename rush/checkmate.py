def checkmate(board_string):
    rows = board_string.strip().split("\n")
    board = [list(row) for row in rows]

    size = len(board)

    if size == 0:
        print("Error")
        return

    for row in board:
        if len(row) != size:
            print("Error")
            return

    king_count = 0
    king_pos = None

    for i in range(size):
        for j in range(size):
            if board[i][j] == 'K':
                king_count += 1
                king_pos = (i, j)
            if board[i][j] not in {'.', 'K', 'Q', 'R', 'B', 'P'}:
                print("Error")
                return
    # print(king_count, king_pos)
    if king_count != 1:
        print("Error")
        return

    king_row, king_col = king_pos


    for i in range(size):
        for j in range(size):
            piece = board[i][j]

            if piece == 'P':
                # print(f"P at {i},{j}")
                if pawn_attack(board, i, j, king_row, king_col):
                    print("Success")
                    return

            elif piece == 'R':
                # print(f"R at {i},{j}")
                if rook_attack(board, i, j, king_row, king_col):
                    print("Success")
                    return

            elif piece == 'B':
                # print(f"B at {i},{j}")
                if bishop_attack(board, i, j, king_row, king_col):
                    print("Success")
                    return

            elif piece == 'Q':
                # print(f"Q at {i},{j}")
                if queen_attack(board, i, j, king_row, king_col):
                    print("Success")
                    return

    print("Fail")

def pawn_attack(board, p_row, p_col, k_row, k_col):
    if p_row - 1 == k_row and abs(p_col - k_col) == 1:
        return True
    return False

def rook_attack(board, r_row, r_col, k_row, k_col):
    if r_row == k_row: 
        step = 1 if k_col > r_col else -1 
        for c in range(r_col + step, k_col, step):
            if board[r_row][c] != '.' and board[r_row][c] != 'K': 
                return False 
        return True 
    elif r_col == k_col:
        step = 1 if k_row > r_row else -1 
        for r in range(r_row + step, k_row, step):
            if board[r][r_col] != '.' and board[r][r_col] != 'K':
                return False 
        return True 
    return False

def bishop_attack(board, b_row, b_col, k_row, k_col):
    if abs(b_row - k_row) == abs(b_col - k_col):
        row_step = 1 if k_row > b_row else -1
        col_step = 1 if k_col > b_col else -1
        r, c = b_row + row_step, b_col + col_step
        while r != k_row and c != k_col:
            if board[r][c] != '.':
                return False
            r += row_step
            c += col_step
        return True
    return False

def queen_attack(board, q_row, q_col, k_row, k_col):
    return rook_attack(board, q_row, q_col, k_row, k_col) or bishop_attack(board, q_row, q_col, k_row, k_col)