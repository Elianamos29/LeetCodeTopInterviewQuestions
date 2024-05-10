from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lp = 0
        rp = len(numbers) - 1
        while True:
            sum = numbers[lp] + numbers[rp]
            if sum == target:
                return [lp + 1, rp + 1]
            elif sum > target:
                rp -= 1
            else:
                lp += 1

if __name__ == '__main__':
    s = Solution()
    numbers = [2,6,7,11,15]
    target = 9
    print(s.twoSum(numbers, target))