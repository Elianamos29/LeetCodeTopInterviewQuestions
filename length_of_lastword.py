from typing import List

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        else:
            return len(s.split()[-1])

if __name__ == '__main__':
    s = Solution()
    string = " Hello W orld "
    print(s.lengthOfLastWord(string))