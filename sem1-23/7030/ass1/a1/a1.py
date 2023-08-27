""" A fancy tic-tac-toe game for CSSE1001/7030 A1. """
from constants import *

Board = list[list[str]]
Pieces = list[int]
Move = tuple[int, int, int]
E = ' '


# Write your functions here
def num_hours() -> float:
    return 130.7


def generate_initial_pieces(num_pieces: int) -> Pieces:
    pieces = list(range(1, num_pieces + 1))
    return pieces


def initial_state() -> Board:
    board = []
    for space in range(GRID_SIZE):
        row = [EMPTY] * GRID_SIZE
        board.append(row)
    return board


def place_piece(board: Board, player: str, pieces_available: Pieces,
                move: Move):
    row, column, piece_size = move[0], move[1], move[2]
    piece = player + str(piece_size)
    board[row][column] = piece
    pieces_available.remove(piece_size)
    return board


def print_game(board: Board, naught_pieces: Pieces,
               cross_pieces: Pieces) -> None:
    n_pieces = []
    for piece in naught_pieces:
        n_pieces.append(str(piece))
    naught = NAUGHT + " has: " + ", ".join(n_pieces)
    print(naught)
    c_pieces = []
    for piece in cross_pieces:
        c_pieces.append(str(piece))
    cross = CROSS + " has: " + ", ".join(c_pieces)
    print(cross)
    # print(NAUGHT + " has: " + str(naught_pieces[0]), end='')
    # for x in naught_pieces[1:]:
    #     print("," + E + str(x), end='')
    # print("\n" + CROSS + " has: " + str(cross_pieces[0]), end='')
    # for y in cross_pieces[1:]:
    #     print("," + E + str(y), end='')
    #  棋盘格
    #  第一二行
    print("\n" + E, end='')
    for n in range(len(board)):
        print(EMPTY + str(n + 1), end='')
    print("\n" + EMPTY + len(board) * 3 * "-")
    #  下面部分(已改名
    r_num = 1
    for row in board:
        print(str(r_num), end='')
        r_num += 1
        for column in row:
            if column == '  ':
                print("|" + EMPTY, end='')
            else:
                print("|" + column, end='')

        print("|")
        print(E * 2 + len(board) * 3 * "-")


# i = initial_state()
# naught_pieces = generate_initial_pieces(6)
# cross_pieces = generate_initial_pieces(6)
# print_game(i, naught_pieces, cross_pieces)
# place_piece(i, NAUGHT, naught_pieces, (1, 1, 2))
# y = place_piece(i, CROSS, cross_pieces, (0, 0, 3))
# print_game(y, naught_pieces, cross_pieces)


def process_move(move: str) -> Move | None:
    elements = move.split()
    row = elements[0]
    if len(elements) == 3:
        column = elements[1]
        peace = elements[2]
    if len(move) != 5:
        print(INVALID_FORMAT_MESSAGE)
    elif len(elements) != 3:
        print(INVALID_FORMAT_MESSAGE)
    elif not row.isdigit() or not 0 < int(row) <= GRID_SIZE:
        print(INVALID_ROW_MESSAGE)
    elif not column.isdigit() or not 0 < int(column) <= GRID_SIZE:
        print(INVALID_COLUMN_MESSAGE)
    elif not peace.isdigit() or not 0 < int(peace) <= PIECES_PER_PLAYER:
        print(INVALID_SIZE_MESSAGE)
    else:
        result = (int(row) - 1, int(column) - 1, int(peace))
        return result


def get_player_move() -> Move:
    while True:
        move_play = input("Enter your move: ")
        if move_play.lower() == "h":
            print(
                "Enter a row, column & piece size in the format: row col size")
            continue
        else:
            elements = move_play.split()
            row = elements[0]
            if len(elements) == 3:
                column = elements[1]
                peace = elements[2]
            if len(move_play) != 5:
                print(INVALID_FORMAT_MESSAGE)
            elif len(elements) != 3:
                print(INVALID_FORMAT_MESSAGE)
            elif not row.isdigit() or not 0 < int(row) <= GRID_SIZE:
                print(INVALID_ROW_MESSAGE)
            elif not column.isdigit() or not 0 < int(column) <= GRID_SIZE:
                print(INVALID_COLUMN_MESSAGE)
            elif not peace.isdigit() or not 0 < int(peace) <= PIECES_PER_PLAYER:
                print(INVALID_SIZE_MESSAGE)
            else:
                result = (int(row) - 1, int(column) - 1, int(peace))
                return result
            continue


def check_move(board: Board, pieces_available: Pieces, move: Move) -> bool:
    row = move[0]
    column = move[1]
    piece_size = move[2]
    if piece_size not in pieces_available:
        return False
    if board[row][column] == EMPTY or board[row][column][1] < str(piece_size):
        return True
    return False


def check_win(board: Board) -> str | None:
    r_elements = []
    for r_row in board:
        for r_column in r_row:
            r_elements.append(r_column[0])
    for r_cut in range(GRID_SIZE):
        r_separate = r_elements[r_cut * GRID_SIZE:(r_cut + 1) * GRID_SIZE]
        r_cut += 1
        for r_pieces in r_separate:
            first_element = r_pieces[0]
            for element in r_pieces:
                if element != first_element:
                    continue
        return first_element
    #  判断行相同
    c_elements = []
    for c_row in range(GRID_SIZE):
        for c_column in range(GRID_SIZE):
            c_elements.append(board[c_column][c_row])
    for c_cut in range(GRID_SIZE):
        c_separate = c_elements[c_cut * GRID_SIZE:(c_cut + 1) * GRID_SIZE]
        c_cut += 1
        for c_pieces in c_separate:
            first_element = c_pieces[0]
            for element in c_pieces:
                if element != first_element:
                    continue
        return first_element
    #  判断列相同
    d_elements = []
    for i in range(GRID_SIZE):
        d_elements.append(board[i][i])
    for d_pieces in d_elements:
        first_element = d_pieces[0]
        for element in d_pieces:
            if element != first_element:
                continue
        return first_element
    #  判断左上到右下对角线
    dd_elements = []
    for i in range(GRID_SIZE):
        dd_elements.append(board[i][GRID_SIZE - (i + 1)])
    for dd_pieces in dd_elements:
        first_element = dd_pieces[0]
        for element in dd_pieces:
            if element != first_element:
                continue
        return first_element
    #  判断右上到左下对角线


def check_stalemate(board: Board, naught_pieces: Pieces, cross_pieces: Pieces) -> bool:
    n_elements = []
    c_elements = []
    for row in board:
        for column in row:
            if column[0] == NAUGHT:
                n_elements.append(column[1])
            else:
                c_elements.append(column[1])
    for c_element in c_elements:
        for n_piece in naught_pieces:
            if n_piece > int(c_element):
                return False
    for n_element in n_elements:
        for c_piece in cross_pieces:
            if c_piece > int(n_element):
                return False
    return True


def main() -> None:
    # Write your main code here
    board = initial_state()
    naught_pieces = generate_initial_pieces(PIECES_PER_PLAYER)
    cross_pieces = generate_initial_pieces(PIECES_PER_PLAYER)
    while True:
        print()
        print(NAUGHT + " turn to move")
        print()


if __name__ == '__main__':
    main()
