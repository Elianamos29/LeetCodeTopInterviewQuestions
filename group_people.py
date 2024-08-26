from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        ans = []
        groups = {}

        for i in range(len(groupSizes)):
            if groupSizes[i] not in groups:
                groups[groupSizes[i]] = [i]
            else:
                groups[groupSizes[i]].append(i)
            if len(groups[groupSizes[i]]) == groupSizes[i]:
                ans.append(groups[groupSizes[i]])
                groups[groupSizes[i]] = []
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.groupThePeople([3, 3, 3, 3, 3, 1, 3]))  # [[0, 1, 2], [3, 4, 6], [5]]
    print(s.groupThePeople([2, 1, 3, 3, 3, 2]))  # [[0, 5], [1], [2, 3, 4]]