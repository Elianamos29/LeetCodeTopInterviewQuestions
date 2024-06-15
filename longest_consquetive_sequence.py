from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n_s = sorted(nums)
        ans = -1
        max_l = 1

        for i in range(len(nums)):
            if ans == -1:
                ans = 1
            else:
                if n_s[i] - n_s[i-1] == 1:
                    ans += 1
                    max_l = max(max_l, ans)
                elif n_s[i] - n_s[i-1] == 0:
                    continue
                else:
                    ans = 1
        if ans == -1:
            return 0
        else:
            return max_l

if __name__ == '__main__':
    s = Solution()
    nums = [100, 4, 200, 1, 3, 2]
    print(s.longestConsecutive(nums)) # 4
    nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    print(s.longestConsecutive(nums)) # 9
    nums = [1, 2, 0, 1]
    print(s.longestConsecutive(nums)) # 3