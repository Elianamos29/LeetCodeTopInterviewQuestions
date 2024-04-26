from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        h = 0
        for i in range(len(citations), 0, -1):
            if citations[i - 1] >= h + 1:
                h += 1
        return h

if __name__ == '__main__':
    s = Solution()
    citations = [3, 0, 6, 1, 5]
    print(s.hIndex(citations))