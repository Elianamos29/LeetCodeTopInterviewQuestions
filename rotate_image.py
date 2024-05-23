import copy
from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        temp = copy.deepcopy(matrix)
        print(temp)
        for i in range(n):
            for j in range(n):
                matrix[i][j] = temp[n-j-1][i]

if __name__ == '__main__':
    s = Solution()
    arr = [[7,4,1],[8,5,2],[9,6,3]]
    s.rotate(arr)
    print(arr)