class Solution:
    def validPalindrome(self, s: str) -> bool:
        if len(s) < 3:
            return True
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                removeL, removeR = s[l+1:r+1], s[l:r]
                return (removeL == removeL[::-1] or removeR == removeR[::-1])
            l += 1
            r -= 1
        return True

if __name__ == '__main__':
    s = Solution()
    print(s.validPalindrome("aba")) # True
    print(s.validPalindrome("abca")) # True
    print(s.validPalindrome("abc")) # False
    print(s.validPalindrome("a")) # True
    print(s.validPalindrome("ab")) # True
    print(s.validPalindrome("abb")) # True
    print(s.validPalindrome("abba")) # True
    print(s.validPalindrome("abbca")) # True
    print(s.validPalindrome("abcbca")) # True
    print(s.validPalindrome("abccba")) # True