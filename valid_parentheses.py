class Solution:
    def isValid(self, s: str) -> bool:
        chars = {')': '(', '}': '{', ']':'['}
        stack = []

        for i in range(len(s)):
            if s[i] in chars.keys():
                if stack and chars[s[i]] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[i])
        
        return len(stack) == 0

if __name__ == '__main__':
    s = Solution()
    print(s.isValid("([])"))
    print(s.isValid("([)]"))
    print(s.isValid("{[]}"))