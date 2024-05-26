class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hash_rn = {}
        hash_mg = {}

        for c in ransomNote:
            hash_rn[c] = hash_rn.get(c, 0) + 1
        for c in magazine:
            hash_mg[c] = hash_mg.get(c, 0) + 1

        for c in ransomNote:
             if c not in magazine:
                return False
             if hash_rn[c] > hash_mg[c]:
                return False

        return True

if __name__ == '__main__':
    s = Solution()
    print(s.canConstruct('a', 'b'))  # False
    print(s.canConstruct('aa', 'ab'))  # False
    print(s.canConstruct('aa', 'aab'))  # True
    print(s.canConstruct('aa', 'aab'))  # True
    print(s.canConstruct('ab', 'aab'))  # True