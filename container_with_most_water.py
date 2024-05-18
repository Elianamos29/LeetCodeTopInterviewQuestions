from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        most = 0
        left = 0
        right = n - 1
        for i in range(n - 1):
            most = max(most, (right - left) * min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1 
        
        return most


if __name__ == '__main__':
    s = Solution()
    height = [1,8,6,2,5,4,8,3,7]
    print(s.maxArea(height)) # Output: 49
    height = [1,1]
    print(s.maxArea(height)) # Output: 1
    height = [10,9,8,7,6,5,4,3,2,1]
    print(s.maxArea(height)) # Output: 25
    height = [1,1,1,1,1,1,1,1,1,1]
    print(s.maxArea(height)) # Output: 9