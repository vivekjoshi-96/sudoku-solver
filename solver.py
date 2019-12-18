"""
A board is a 9 X 9 grid
Each cell contains a value from 0-9
The board is Represented using a list of lists(9)
A valid row/column has values from 1-9 and no two cells have the same values
Box is a smaller 3X3 grid, there are three boxes on one board
A valid box also contains values from 1-9 and all cells have unique values
"""


def main():
    board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]
    print(*board, sep='\n')


if __name__ == '__main__':
    main()

