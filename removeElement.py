from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = nums.count(val)
        for i in range(count):
            nums.remove(val)
        
        return (len(nums))

if __name__ == '__main__':
    s = Solution()
    nums = [3,2,2,3]
    val = 3
    print(s.removeElement(nums, val))
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    print(s.removeElement(nums, val))