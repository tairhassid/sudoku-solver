from typing import List


class Sudoku:
    """A class used to solve a Sudoku board

    Attributes
    ----------
    Sudoku.n : int
        the game board dimension - nxn board
    Sudoku.box_len : int
        the dimension of a single box of the board - square root of n
    board : list[list[int]]
        the game board

    Methods
    -------
    solve()
        fills the board with the solution
    """
    n = 9
    box_len = 3

    def __init__(self, board: List[List[int]]):
        """
        Parameter
        ---------
        board: list[list[int]]
            the game board- list of lists of int
        """
        self.board = []
        self.set_board(board)

    def solve(self):
        return self.__solve_sudoku(0, 0)

    def __solve_sudoku(self, row, col):
        """finds a solution for the sudoku board
            using a recursive backtracking algorithm

        Parameters
        ----------
        row: int
        col: int

        Return
        ------
        bool
            true if a solution exists,
            false if a solution doesn't exist
        """
        if row == self.n - 1 and col == self.n:
            return True

        if col == self.n:
            row = row + 1
            col = 0

        if self.board[row][col] != 0:
            return self.__solve_sudoku(row, col+1)

        for i in range(1, self.n+1):
            if self.__possible_solution(row, col, i):
                self.board[row][col] = i
                if self.__solve_sudoku(row, col+1):
                    return True
            self.board[row][col] = 0

        return False

    def __possible_solution(self, row, col, num):
        """checks if a number is a possible solution for an index

        Parameters
        ----------
        row: int
        col: int
        num: int
            a number suspected to be a possible solution

        Return
        ------
        bool
            true if the number is a possible solution
            a possible solution is a number that does not exist in
            the same row/column/square more then once.
        """
        # if the number exists in the row
        if num in self.board[row] and self.board[row][col] != num:
            return False

        # check if the number exists in this column
        for i in range(len(self.board)):
            if self.board[i][col] == num and i != row:
                return False

        # if the number exists in the nine close cells
        start_pos = self.__find_start_pos(row, col)

        for i in range(self.box_len):
            lst = self.board[start_pos[0] + i][start_pos[1]: start_pos[1] + 2]
            if num in lst:
                return False

        return True

    def __find_start_pos(self, row, col):
        """ search the start position of the square containing
            the row and col

        Parameters
        ----------
        row: int
        col: int

        Return
        ------
        tuple
            the beginning position of the current square
        """
        return self.__compute_index(row), self.__compute_index(col)

    def __compute_index(self, idx):
        """ computes the first index of the current square
            (left most for column/upper most for row)

        Parameters
        ----------
        idx: int
            an index on the board
        Return
        -------
        int
            the left most/upper most index for row/col respectively
        """
        return (idx // self.box_len) * self.box_len

    def set_board(self, board):
        """
        sets the board class property

        :param board: List[List[int]]
            the game board
        :exception
            jf the numbers are not 0-9 or the board is not 9x9
        """
        if len(board) == self.n and all(len(i) == self.n for i in board):
            bool_lst = (all([0 <= j <= 9 for j in lst]) for lst in board)
            if all(bool_lst):
                self.board = board
            else:
                raise Exception("The numbers should be between 1 and 9, 0 for the empty cells")
        else:
            raise Exception("The board should be 9X9")

    def __str__(self):
        s = ""
        for i in range(len(self.board)):
            if i != 0 and i % 3 == 0:
                s = s + "_ _ _ _ _ _ _ _ _ _ _\n"
            for j in range(len(self.board)):
                if j != 0 and j % 3 == 0:
                    s = s + "| "
                s = s + str(self.board[i][j]) + " "

            s = s + "\n"
        return s


