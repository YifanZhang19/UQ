# def FirstPython() -> str:
#     print("Hello, World!")
#
# FirstPython()

board = [['p1', 'EMPTY', 'EMPTY'], ['O1', 'O2', 'O3'], ['O1', 'EMPTY', 'EMPTY']]
def check_win1(board):
    ppp = []
    for c_column in range(3):
        c_elements = []
        for c_row in range(3):
            c_elements.append(board[c_row][c_column])
        ppp.append(c_elements)

    for row in ppp:
        if row[0] != 'EMPTY':
            all_equal = True
            for item in row:
                if item[0] != row[0][0]:
                    all_equal = False
                    break
            if all_equal:
                return row[0][0]
    return None

print(check_win1(board))



