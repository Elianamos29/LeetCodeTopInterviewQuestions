from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = 0
        l, r = 0, 1
        while r < len(prices):
            if prices[r] <= prices[l]:
                l = r
            else:
                profit = prices[r] - prices[l]
                if profit > max:
                    max = profit
            r += 1
        return max
    
if __name__ == '__main__':
    s = Solution()
    prices = [7, 1, 5, 3, 6, 4]
    print(s.maxProfit(prices))