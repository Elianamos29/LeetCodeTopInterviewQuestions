from typing import List

class Solution:
    def intToRoman(self, num: int) -> str:
        roman = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
        n = 0
        roman_num = ""
        while num > 0:
            if num >= 1000:
                n = num // 1000
                roman_num += n * roman[1000]
                num -= n * 1000
            elif num >= 500:
                if num >= 900:
                    roman_num += roman[100] + roman[1000]
                    num -= 900
                else:
                    n = num // 500
                    roman_num += n * roman[500]
                    num -= n * 500
            elif num >= 100:
                if num >= 400:
                    roman_num += roman[100] + roman[500]
                    num -= 400
                else:
                    n = num // 100
                    roman_num += n * roman[100]
                    num -= n * 100
            elif num >= 50:
                if num >= 90:
                    roman_num += roman[10] + roman[100]
                    num -= 90
                else:
                    n = num // 50
                    roman_num += n * roman[50]
                    num -= n * 50
            elif num >= 10:
                if num >= 40:
                    roman_num += roman[10] + roman[50]
                    num -= 40
                else:
                    n = num // 10
                    roman_num += n * roman[10]
                    num -= n * 10
            elif num >= 5:
                if num == 9:
                    roman_num += roman[1] + roman[10]
                    num -= 9
                else:
                    n = num // 5
                    roman_num += n * roman[5]
                    num -= n * 5
            elif num >= 1:
                if num == 4:
                    roman_num += roman[1] + roman[5]
                    num -= 4
                else:
                    n = num // 1
                    roman_num += n * roman[1]
                    num -= n * 1
        return roman_num

if __name__ == '__main__':
    s = Solution()
    num = 1994
    print(s.intToRoman(num))