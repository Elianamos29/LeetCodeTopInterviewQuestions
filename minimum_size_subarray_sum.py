from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        ans = n + 1
        left = 0
        sum = 0

        for i in range(n):
            sum += nums[i]
            while sum >= target:
                ans = min(ans, i - left + 1)
                sum -= nums[left]
                left += 1
        return ans if ans != n + 1 else 0


if __name__ == '__main__':
    s = Solution()
    print(s.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))  # 2
    print(s.minSubArrayLen(4, [1, 4, 4]))  # 1