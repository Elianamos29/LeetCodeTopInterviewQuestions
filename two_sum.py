from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) - 1
        nums = [(i, n) for i, n in enumerate(nums)]
        print(nums)
        nums.sort(key=lambda x: x[1])
        print(nums)
        while l < r:
            if nums[l][1] + nums[r][1] == target:
                return [nums[l][0], nums[r][0]]
            else:
                if nums[l][1] + nums[r][1] < target:
                    l += 1
                else:
                    r -= 1
        return [-1, -1]

if __name__ == '__main__':
    s = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    print(s.twoSum(nums, target)) # [0, 1]
    nums = [3, 3]
    target = 6
    print(s.twoSum(nums, target)) # [0, 1]
    nums = [-1, -2, -3, -4, -5]
    target = -8
    print(s.twoSum(nums, target)) # [2, 4]