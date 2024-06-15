from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i = 0
        hash_n = {}

        while i < len(nums):
            if nums[i] in hash_n and i - k <= hash_n[nums[i]]:
                return True
            hash_n[nums[i]] = i
            i += 1
        
        return False

if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3, 1]
    k = 3
    print(s.containsNearbyDuplicate(nums, k)) # True
    nums = [1, 0, 1, 1]
    k = 1
    print(s.containsNearbyDuplicate(nums, k)) # True
    nums = [1, 2, 3, 1, 2, 3]
    k = 2
    print(s.containsNearbyDuplicate(nums, k)) # False