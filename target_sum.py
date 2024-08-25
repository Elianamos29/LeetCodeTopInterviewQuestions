from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        hash = {}
        def ways(index, total):
            if index == len(nums):
                return 1 if total == target else 0
            if (index, total) in hash:
                return hash[(index, total)]
            
            hash[(index, total)] = (
                ways(index + 1, total + nums[index]) +
                ways(index + 1, total - nums[index])
            )

            return hash[(index, total)]
        return ways(0, 0)


if __name__ == '__main__':
    s = Solution()
    nums = [1, 1, 1, 1, 1]
    target = 3
    print(s.findTargetSumWays(nums, target)) # 5
    nums = [1]
    target = 1
    print(s.findTargetSumWays(nums, target)) # 1
    nums = [1]
    target = 2
    print(s.findTargetSumWays(nums, target)) # 0
    nums = [1, 2, 3]
    target = 6
    print(s.findTargetSumWays(nums, target)) # 1