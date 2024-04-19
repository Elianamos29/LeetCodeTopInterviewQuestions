from typing import List


def reverse(nums, start, end):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        k = k % l
        
        reverse(nums, 0, l - 1)
        reverse(nums, 0, k - 1)
        reverse(nums, k, l - 1)

if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    s.rotate(nums, k)
    print(nums)