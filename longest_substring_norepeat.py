class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        left = 0
        right = 0
        hash_map = {}

        while right < n:
            if s[right] in hash_map:
                left = max(hash_map[s[right]] + 1, left)
            hash_map[s[right]] = right
            ans = max(ans, right - left + 1)
            right += 1   
        
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring('abcabcbb'))  # 3
    print(s.lengthOfLongestSubstring('bbbbb'))  # 1
    print(s.lengthOfLongestSubstring('pwwkew'))  # 3
    print(s.lengthOfLongestSubstring(''))  # 0
    print(s.lengthOfLongestSubstring(' '))  # 1
    print(s.lengthOfLongestSubstring('au'))  # 2
    print(s.lengthOfLongestSubstring('dvdf'))  # 3
    print(s.lengthOfLongestSubstring('aab'))  # 2
    print(s.lengthOfLongestSubstring('abba'))  # 2
