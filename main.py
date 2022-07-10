from collections import defaultdict


# At a high level, we can think of the problem as follows:
# A board is valid if there are no duplicates in any row, column, or 3x3 box.
# Because of this we are going to iterate through every space, cache the values in hashsets as we go,
# and check if the current value is in any of the 3 corresponding hashsets.
# If it is, we return false.
# If we iterate through every space and don't find any duplicates, we return true.
def valid_sudoku(board):
    # Using default dicts as our data structure so that I don't have to explicitly create keys for each row, column, and box.
    cols = defaultdict(set)
    rows = defaultdict(set)
    squares = defaultdict(set)
    # Iterate through the board.
    for i in range(9):
        for j in range(9):
            # If the current cell is empty, continue.
            if board[i][j] == ".":
                continue
            num = int(board[i][j])
            # Check if the number is already in the row, column, or square. If so, return False.
            if num in rows[i] or num in cols[j] or num in squares[(i // 3, j // 3)]:
                return False
            # Finally at the end of every iteration we add this number to the row, column, and square so we know if we see a duplicate.
            cols[j].add(num)
            rows[i].add(num)
            squares[(i // 3, j // 3)].add(num)
    return True


def main():
    print(
        valid_sudoku(
            [
                ["5", "3", ".", ".", "7", ".", ".", ".", "."],
                ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                [".", "9", "8", ".", ".", ".", ".", "6", "."],
                ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", "6", ".", ".", ".", ".", "2", "8", "."],
                [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"],
            ]
        )
    )


if __name__ == "__main__":
    main()

# Tests
def test_1():
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    assert valid_sudoku(board) == True


def test_2():
    board = [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    assert valid_sudoku(board) == False
