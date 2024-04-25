from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps, end, farthest = 0, 0, 0
        for i in range(len(nums)):
            farthest = max(farthest, nums[i] + i)
            if i == end and i != len(nums) - 1:
                jumps += 1
                end = farthest
        return jumps

if __name__ == '__main__':
    s = Solution()
    nums = [2, 3, 1, 1, 4]
    print(s.jump(nums))