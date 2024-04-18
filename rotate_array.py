from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        for i in range(k):
            arr = nums.copy()
            for j in range(l - 1):
                nums[j + 1] = arr[j]
            nums[0] = arr[l-1]