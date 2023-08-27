from constants import *
Board = list[list[str]]
Pieces = list[int]
Move = tuple[int, int, int]

E = ' '
board = [['O1', EMPTY, EMPTY], ['O1', 'O2', 'O3'], ['O1', EMPTY, EMPTY]]
def check_win1(board):
    #检查行
    for row in board:
        if row[0] != EMPTY:
            all_equal = True
            for item in row:
                if item != row[0]:
                    all_equal = False
                    break
            if all_equal:
                return row[0]

    # 检查列
    for col in range(GRID_SIZE):
        col_values = [board[row][col] for row in range(GRID_SIZE)]
        if col_values[0][0] != EMPTY:
            all_same = True
            for item in col_values:
                if item[0] != col_values[0][0]:
                    all_same = False
                    break
            if all_same:
                return col_values[0][0]

    # # 检查对角线1
    # diag1_values = [board[i][i] for i in range(GRID_SIZE)]
    # if diag1_values[0] != EMPTY:
    #     all_equal = True
    #     for item in diag1_values:
    #         if item != diag1_values[0]:
    #             all_equal = False
    #             break
    #     if all_equal:
    #         return diag1_values[0]

    # # 检查对角线2
    # diag2_values = [board[i][GRID_SIZE - 1 - i] for i in range(GRID_SIZE)]
    # if diag2_values[0] != EMPTY:
    #     all_equal = True
    #     for item in diag2_values:
    #         if item != diag2_values[0]:
    #             all_equal = False
    #             break
    #     if all_equal:
    #         return diag2_values[0]

    return None

print(check_win1(board))



"""
-------------------------------------------------------------------------------------------------------------------------------------------
"""
def check_win2(board):
    # 检查行
    for row in board:
        if row[0][0] != EMPTY:
            all_same = True
            for item in row:
                if item[0] != row[0][0]:
                    all_same = False
                    break
            if all_same:
                return row[0][0]

    # 检查列
    for col in range(GRID_SIZE):
        col_values = [board[row][col] for row in range(GRID_SIZE)]
        if col_values[0][0] != EMPTY:
            all_same = True
            for item in col_values:
                if item[0] != col_values[0][0]:
                    all_same = False
                    break
            if all_same:
                return col_values[0][0]

    # 检查对角线1
    diag1_values = [board[i][i] for i in range(GRID_SIZE)]
    if diag1_values[0][0] != EMPTY:
        all_same = True
        for item in diag1_values:
            if item[0] != diag1_values[0][0]:
                all_same = False
                break
        if all_same:
            return diag1_values[0][0]

    # 检查对角线2
    diag2_values = [board[i][GRID_SIZE - 1 - i] for i in range(GRID_SIZE)]
    if diag2_values[0][0] != EMPTY:
        all_same = True
        for item in diag2_values:
            if item[0] != diag2_values[0][0]:
                all_same = False
                break
        if all_same:
            return diag2_values[0][0]

    return None

