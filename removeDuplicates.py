from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        last_unique_index = 0
        for i in range(1, len(nums)):
            if nums[last_unique_index] != nums[i]:
                nums[last_unique_index + 1] = nums[i]
                last_unique_index += 1
        
        return last_unique_index + 1

if __name__ == '__main__':
    s = Solution()
    nums = [1,1,2]
    print(s.removeDuplicates(nums))
    nums = [0,0,1,1,1,2,2,3,3,4]
    print(s.removeDuplicates(nums))