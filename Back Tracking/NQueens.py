# N Queens Problem: Given an integer n, find all distinct solutions to the n-queens puzzle.

class Solution:
    def __init__(self):
        self.result = []
        self.board = [[0 for i in range(9)] for i in range(9)]

    # go through the current board and convert to string
    def answerAdd(self, n):
        currentBoard = []
        for i in range(n):
            temp = ""
            for j in range(n):
                if self.board[i][j] != 0:
                    temp += "Q"
                else:
                    temp += "."
            currentBoard.append(temp)
        self.result.append(currentBoard)

    def isSafe(self, row, col, n):
        # check for row and col
        for i in range(col):
            if self.board[row][i] != 0:
                return False

        for i in range(row):
            if self.board[i][col] != 0:
                return False

        # check up and down the diagonals
        i, j = row, col
        while i >= 0 and j >= 0:
            if self.board[i][j]:
                return False
            i, j = i - 1, j - 1

        i, j = row, col
        while i < n and j >= 0:
            if self.board[i][j]:
                return False
            i, j = i + 1, j - 1

        i, j = row, col
        while i >= 0 and j < n:
            if self.board[i][j]:
                return False
            i, j = i - 1, j + 1

        i, j = row, col
        while i < n and j < n:
            if self.board[i][j]:
                return False
            i, j = i + 1, j + 1

        return True

    def solve(self, col, n):
        if col == n:
            self.answerAdd(n)
            return

        for i in range(n):
            if self.isSafe(i, col, n):
                self.board[i][col] = 1
                self.solve(col + 1, n)
                self.board[i][col] = 0
        return

    def solveNQueens(self, n):
        self.solve(0, n)
        return self.result


def main():
    mySol = Solution()
    print("Different solutions for placing 5 queens on a board are ")
    print(mySol.solveNQueens(5))


if __name__ == "__main__":
    main()
