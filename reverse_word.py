class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.strip().split()[::-1])

if __name__ == '__main__':
    s = Solution()
    string = "example         good a    "
    print(s.reverseWords(string)) # Output: 'blue is sky the