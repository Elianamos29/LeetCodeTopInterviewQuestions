from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count, res = 0, 0

        for n in nums:
            if count == 0:
                res = n
            count += (1 if n == res else -1)
        return res

if __name__ == '__main__':
    s = Solution()
    nums = [3,2,3]
    print(s.majorityElement(nums))
    nums = [2,2,1,1,1,2,2]
    print(s.majorityElement(nums))
    nums = [1]
    print(s.majorityElement(nums))