class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_c = {}

        for i in range(len(s)):
            if t[i] not in map_c:
                if s[i] in map_c.values():
                    return False
                map_c[t[i]] = s[i]
            if map_c[t[i]] != s[i]:
                return False
        return True

if __name__ == '__main__':
    s = Solution()
    print(s.isIsomorphic('egg', 'add'))  # True
    print(s.isIsomorphic('foo', 'bar'))  # False
    print(s.isIsomorphic('paper', 'title'))  # True