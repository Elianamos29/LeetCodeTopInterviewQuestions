class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ci = 0
        for i in range(len(s)):
            t = t[ci:]
            if s[i] in t:
                index = t.index(s[i])
                ci = index + 1
            else:
                return False
                
        return True

if __name__ == '__main__':
    sl = Solution()
    s = "aaaaaa"
    t = "bbaaaa"
    print(sl.isSubsequence(s, t))