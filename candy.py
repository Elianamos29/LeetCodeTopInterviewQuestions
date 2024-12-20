from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i - 1] + 1
        
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i+1] and candies[i] <= candies[i+1]:
                candies[i] = candies[i+1] + 1
            
        return sum(candies)
    
if __name__ == '__main__':
    s = Solution()
    ratings = [1, 0, 2]
    print(s.candy(ratings))
    ratings = [1, 2, 2]
    print(s.candy(ratings))
        