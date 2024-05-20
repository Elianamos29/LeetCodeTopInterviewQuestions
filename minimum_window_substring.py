def is_valid(hash_s, hash_t):
            for k, v in hash_t.items():
                if k not in hash_s:
                    return False
                if hash_s[k] < v:
                    return False
            return True

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        n = len(t)
        hash_t = {}
        hash_s = {}

        for c in t:
            hash_t[c] = hash_t.get(c, 0) + 1
        
        for c in s:
            hash_s[c] = 0

        if n > m:
            return ""
        
        left = 0
        ans = ""
        min_len = m + 1
        i = 0

        while i < m:
            if s[i] in hash_t:
                hash_s[s[i]] += 1
                while is_valid(hash_s, hash_t):
                    if i - left + 1 < min_len:
                        min_len = i - left + 1
                        ans = s[left:i + 1]
                    if s[left] in hash_t:
                        hash_s[s[left]] -= 1
                    left += 1
            i += 1
        
        return ans

if __name__ == '__main__':
    s = Solution()
    S = "ADOBECODEBANC"
    T = "ABC"
    print(s.minWindow(S, T)) # BANC
    S = "a"
    T = "a"
    print(s.minWindow(S, T)) # a
    S = "a"
    T = "aa"
    print(s.minWindow(S, T)) # ""
    S = "a"
    T = "b"
    print(s.minWindow(S, T)) # ""
    S = "aa"
    T = "aa"
    print(s.minWindow(S, T)) # aa
    S = "aa"
    T = "aaa"
    print(s.minWindow(S, T)) # ""
    S = "aa"
    T = "a"
    print(s.minWindow(S, T)) # a
    S = "bba"
    T = "ab"
    print(s.minWindow(S, T)) # ba
    S = "ab"
    T = "b"
    print(s.minWindow(S, T)) # b
    S = "bba"
    T = "ab"
    print(s.minWindow(S, T)) # ba