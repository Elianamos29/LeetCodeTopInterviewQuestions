from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        l = 0

        for i in range(0, len(nums)):
            if i == 0:
                ans.append("%s" % nums[0])
            elif nums[i] - nums[i-1] == 1:
                ans[-1] = "%s->%s" % (nums[l], nums[i])
            else:
                ans.append("%s" % nums[i])
                l = i
        
        return ans

if __name__ == '__main__':
    s = Solution()
    nums = [0,2,3,4,6,8,9]
    print(s.summaryRanges(nums))