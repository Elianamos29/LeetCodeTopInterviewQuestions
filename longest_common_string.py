from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = strs[0]
        i = 1
        while s and i < len(strs):
            if s not in strs[i][:len(s)]:
                s = s[:-1]
                i = 1
            else:
                i += 1
        return s

if __name__ == '__main__':
    s = Solution()
    string = ["flower", "flow", "flight"]
    print(s.longestCommonPrefix(string)) # Output: 'fl