from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_mult = 1
        r_mult = 1
        l = len(nums)
        l_prod = [0] * l
        r_prod = [0] * l

        for i in range(l):
            j = -i - 1
            l_prod[i] = l_mult
            r_prod[j] = r_mult
            l_mult *= nums[i]
            r_mult *= nums[j]
        
        return [l * r for l, r in zip(l_prod, r_prod)]


if __name__ == '__main__':
    s = Solution()
    print(s.productExceptSelf([1, 2, 3, 4]))  # [24, 12, 8, 6]
    print(s.productExceptSelf([1, 2, 3, 4, 5]))  # [120, 60, 40, 30, 24]