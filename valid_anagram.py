class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
    
if __name__ == '__main__':
    sl = Solution()
    s = 'anagram'
    t = 'granama'
    print(sl.isAnagram(s, t)) # True
    s = 'elianamos'
    t = 'anomalies'
    print(sl.isAnagram(s, t)) # True
    s = 'cat'
    t = 'car'
    print(sl.isAnagram(s, t)) # False