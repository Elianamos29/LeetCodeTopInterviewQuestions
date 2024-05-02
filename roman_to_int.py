from typing import List

class Solution:
    def romanToInt(self, s: str) -> int:
        n = 0
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        n += roman[s[0]]
        for i in range(1, len(s)):
            if roman[s[i]] / roman[s[i-1]] == 5 or roman[s[i]] / roman[s[i-1]] == 10:
                n += (roman[s[i]] - 2 * roman[s[i-1]])
            else:
                n += roman[s[i]]
        return n

if __name__ == '__main__':
    s = Solution()
    roman = "MCMXCIV"
    print(s.romanToInt(roman))