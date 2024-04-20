from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        minp = prices[0]

        for i in range(1, len(prices)):
            if prices[i] < minp:
                minp = prices[i]
            else:
                if prices[i] - minp > max_profit:
                    max_profit = prices[i] - minp
            
        return max_profit
    
if __name__ == '__main__':
    s = Solution()
    prices = [7, 1, 5, 3, 6, 4]
    print(s.maxProfit(prices))