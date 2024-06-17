from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        i = 0
        while i < len(intervals) - 1:
            if intervals[i][1] >= intervals[i + 1][0]:
                intervals[i][1] = max(intervals[i][1], intervals[i + 1][1])
                intervals.pop(i + 1)
            else:
                i += 1
        
        return intervals

if __name__ == '__main__':
    s = Solution()
    print(s.merge([[1,3],[2,6],[8,10],[15,18]])) # [[1,6],[8,10],[15,18]]
    print(s.merge([[1,4],[4,5]])) # [[1,5]]