from typing import List

def is_valid(row: List[str]) -> bool:
    seen = set()
    for cell in row:
        if cell == '.':
            continue
        if cell in seen:
            return False
        seen.add(cell)
    return True

class Solution:
    def isValidSudoku(self, board: List[List: str]) -> bool:
        # check rows
        for row in board:
            if not is_valid(row):
                return False

        # check columns
        for col in range(9):
            if not is_valid([row[col] for row in board]):
                return False

        # check 3x3 squares
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                square = [board[r][c] for r in range(row, row + 3) for c in range(col, col + 3)]
                if not is_valid(square):
                    return False

        return True

if __name__ == '__main__':
    s = Solution()
    board = [["8","3",".",".","7",".",".",".","."],
             ["6",".",".","1","9","5",".",".","."],
             [".","9","8",".",".",".",".","6","."],
             ["8",".",".",".","6",".",".",".","3"],
             ["4",".",".","8",".","3",".",".","1"],
             ["7",".",".",".","2",".",".",".","6"],
             [".","6",".",".",".",".","2","8","."],
             [".",".",".","4","1","9",".",".","5"],
             [".",".",".",".","8",".",".","7","9"]]
    print(s.isValidSudoku(board))  # True