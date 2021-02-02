class Solution:
    def dfs(self, board, i, j, rows, cols):
        if i >= 0 and i < rows and j >= 0 and j < cols and board[i][j] == 'O':
            board[i][j] = '*'
            self.dfs(board, i + 1, j, rows, cols)
            self.dfs(board, i - 1, j, rows, cols)
            self.dfs(board, i, j + 1, rows, cols)
            self.dfs(board, i, j - 1, rows, cols)

    def solve(self, board):

        # get the size of the board
        rows = len(board)
        if rows <= 2:
            return
        cols = len(board[0])
        if cols <= 2:
            return

        # if an O is encountered at one of the boundaries,
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O' and (i == 0 or j == 0 or i == rows - 1 or j == cols - 1):
                    self.dfs(board, i, j, rows, cols)

        # convert the special characters to O and O to X
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '*':
                    board[i][j] = 'O'
        print(board)


def main():
    mySol = Solution()
    board = [["X", "X", "X", "X"], ["X", "O", "O", "X"],
             ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
    print("Regions surrounded by X for the board: ")
    print(board)
    print("are ")
    mySol.solve(board)


if __name__ == "__main__":
    main()
