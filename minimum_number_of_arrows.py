from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        t_ranges = [points[0]]

        for i in range(1, len(points)):
            if points[i][0] > t_ranges[-1][1]:
                t_ranges.append(points[i])
            else:
                t_ranges[-1][0] = points[i][0]
                t_ranges[-1][1] = min(t_ranges[-1][1], points[i][1])

        return len(t_ranges)

if __name__ == '__main__':
    s = Solution()
    print(s.findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]))
    print(s.findMinArrowShots([[1,2],[3,4],[5,6],[7,8]]))
    print(s.findMinArrowShots([[9,12],[1,10],[4,11],[8,12],[3,9],[6,9],[6,7]]))