from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        total_trapped = 0
        for i in range(1, len(height) - 1):
            left = max(height[:i])
            right = max(height[i+1:])
            trapped = min(left, right) - height[i]
            if trapped >= 0:
                total_trapped += trapped

        return total_trapped

if __name__ == '__main__':
    s = Solution()
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(s.trap(height))
    height = [4,2,0,3,2,5]
    print(s.trap(height))