board = [[9, 2, 0,   0, 0, 0,    5, 8, 4],
         [0, 0, 0,   5, 0, 0,    0, 0, 3],
         [0, 8, 3,   0, 9, 2,    0, 0, 0],

         [2, 6, 0,   8, 5, 4,    0, 0, 1],
         [0, 0, 5,   3, 6, 1,    0, 9, 0],
         [1, 0, 0,   0, 0, 9,    0, 0, 0],

         [8, 5, 0,   2, 0, 3,    0, 1, 0],
         [4, 1, 2,   9, 8, 0,    0, 3, 0],
         [3, 9, 0,   0, 0, 6,    8, 0, 0]]


def is_fitting(decimal, row, col, board=board):
    # checking in row
    if decimal in board[row]:
        return False

    for i in range(9):
        # checking in column
        if decimal == board[i][col]:
            return False

        # checking in square
        square_row = 3 * (row // 3) + i//3
        square_col = 3 * (col // 3) + i%3
        if decimal == board[square_row][square_col]:
            return False

    return True


def matching_square(start, row, col, board=board):
    for decimal in range(start, 10):
        if is_fitting(decimal, row, col):
            board[row][col] = decimal
            break


def matching_decimals(cords_of_changables, row, col, board=board):
    to_match = board[row][col]
    matching_square(to_match + 1, row, col)
    is_square_the_same = to_match == board[row][col]
    while is_square_the_same:
        board[row][col] = 0
        prev_index = cords_of_changables.index((row, col)) - 1
        if prev_index < 0:
            raise IndexError
        prev_row, prev_col = cords_of_changables[prev_index]
        matching_decimals(cords_of_changables, prev_row, prev_col)
        matching_square(1, row, col)
        is_square_the_same = board[row][col] == 0


def solve(board=board):
    list_of_cords = []
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                list_of_cords.append((row, col))
                matching_decimals(list_of_cords, row, col)


for row in board:
    print(row)
print()
solve()
for row in board:
    print(row)
