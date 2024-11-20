from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []

        if len(tokens) == 1:
            return tokens[-1]

        for i in range(len(tokens)):
            if tokens[i] in ['+', '-', '/', '*']:
                op2 = int(st.pop())
                op1 = int(st.pop())
                
                if tokens[i] == '+':
                    result = op1 + op2
                elif tokens[i] == '-':
                    result = op1 - op2
                elif tokens[i] == '/':
                    if op2 != 0:
                        result =  int(op1 / op2)
                elif tokens[i] == '*':
                    result = op1 * op2
                st.append(result)
            else:
                st.append(tokens[i])
        
        return st[-1]

if __name__ == '__main__':
    s = Solution()
    print(s.evalRPN(["2", "1", "+", "3", "*"]))  # 9
    print(s.evalRPN(["4","13","5","/","+"])) # 6
    print(s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])) # 22
    print(s.evalRPN(["4","-2","/","2","-3","-","-"])) # -7