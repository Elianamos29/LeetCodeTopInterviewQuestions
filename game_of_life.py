from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        for i in range(m * n):
            x = i // n
            y = i % n
            live = 0
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == 0 and dy == 0:
                        continue
                    if 0 <= x + dx < m and 0 <= y + dy < n:
                        live += board[x + dx][y + dy] & 1
            if board[x][y] == 1:
                if live < 2 or live > 3:
                    board[x][y] = 3
            else:
                if live == 3:
                    board[x][y] = 2
        for i in range(m * n):
            x = i // n
            y = i % n
            if board[x][y] == 2:
                board[x][y] = 1
            if board[x][y] == 3:
                board[x][y] = 0
                

if __name__ == '__main__':
    s = Solution()
    arr = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
    s.gameOfLife(arr)
    print(arr)
    arr = [[1,1],[1,0]]
    s.gameOfLife(arr)
    print(arr)