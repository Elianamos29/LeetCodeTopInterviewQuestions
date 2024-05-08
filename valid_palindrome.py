class Solution:
    def isPalindrome(self, s: str) -> bool:
        sen = ''
        for c in s:
            if c.isalnum():
                sen += c.lower()
        if sen == sen[::-1]:
            return True
        return False

if __name__ == '__main__':
    s = Solution()
    input = "A man, a plan, a canal: Panama"
    inp = "0P"
    print(s.isPalindrome(input))
    print(s.isPalindrome(inp))