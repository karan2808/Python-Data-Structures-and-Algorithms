# SudokuSolver: Program to solve a sudoku puzzle. 

class Solution:
    def __init__(self, board):
        self.board = board
    # check if you can solve the board

    def solve(self):
        # traverse the board
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                # if a blank is encountered
                if (self.board[i][j] == '.'):
                    # check every character
                    for character in range(1, 10):
                        c = str(character)
                        # if the board is valid
                        if (self.valid(i, j, c)):
                            # set the i, j value to that character
                            self.board[i][j] = c
                            # check if board can be solved, if yes, return true
                            if (self.solve()):
                                return True
                            # revert the change, backtrack
                            else:
                                self.board[i][j] = '.'
                    return False
        return True

    def valid(self, i, j, c):
        for k in range(9):
            if self.board[i][k] != '.' and self.board[i][k] == c:
                return False
            if self.board[k][j] != '.' and self.board[k][j] == c:
                return False
            # if i = 1, 0 + k/3, i = 4, 1 + k/3, i = 7, 2 + k/3...
            if self.board[3 * int(i/3) + int(k/3)][3 * int(j/3) + int(k % 3)] != '.' and self.board[3 * (i//3) + k//3][3 * (j//3) + k % 3] == c:
                return False
        return True

    def solveSudoku(self):
        self.solve()
        return self.board


def main():
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."],
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    mySol = Solution(board)
    print("Original board: ")
    print(board)
    print("Solved board: ")
    print(mySol.solveSudoku())


if __name__ == "__main__":
    main()
