class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        result = 0
        sign = 1
        i = 0

        while i < len(s):
            if s[i].isdigit():
                num = 0
                while i < len(s) and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                result += sign * num
                i -= 1

            elif s[i] == '+':
                sign = 1
            elif s[i] == '-':
                sign = -1

            elif s[i] == '(':
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            
            elif s[i] == ')':
                prev_sign = stack.pop()
                prev_result = stack.pop()
                result = prev_result + prev_sign * result
            
            i += 1
        
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.calculate("1 + 1"))  # 2
    print(s.calculate(" 2-1 + 2 "))  # 3
    print(s.calculate("(1+(4+5+2)-3)+(6+8)"))  # 23
    print(s.calculate("2147483647")) # 2147483647