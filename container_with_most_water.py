from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        most = 0
        for i in range(len(height) - 1):
            for j in range(i + 1, len(height)):
                most = max(most, (j - i) * min(height[i], height[j]))
        
        return most


if __name__ == '__main__':
    s = Solution()
    height = [1,8,6,2,5,4,8,3,7]
    print(s.maxArea(height)) # Output: 49
    height = [1,1]
    print(s.maxArea(height)) # Output: 1
    height = [4,3,2,1,4]
    print(s.maxArea(height)) # Output: 16
    height = [1,2,1]
    print(s.maxArea(height)) # Output: 2
    height = [1,2,4,3]
    print(s.maxArea(height)) # Output: 4
    height = [1,2,3,4,5,6,7,8,9,10]
    print(s.maxArea(height)) # Output: 25
    height = [10,9,8,7,6,5,4,3,2,1]
    print(s.maxArea(height)) # Output: 25
    height = [1,1,1,1,1,1,1,1,1,1]
    print(s.maxArea(height)) # Output: 9