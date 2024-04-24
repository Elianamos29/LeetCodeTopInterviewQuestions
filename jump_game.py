from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxReach = 0
        i = 0
        while i < len(nums) and i <= maxReach:
            maxReach = max(i +  nums[i], maxReach)
            i += 1
        if i == len(nums):
            return True
        return False

if __name__ == '__main__':
    s = Solution()
    nums = [2, 3, 1, 1, 4]
    print(s.canJump(nums))
    nums = [3, 2, 1, 0, 4]
    print(s.canJump(nums))