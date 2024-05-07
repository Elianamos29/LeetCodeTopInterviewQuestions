class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s
        arr = ['' for i in range(numRows)]
        row = 0
        godown = True
        for c in s:
            arr[row] += c
            if row == numRows - 1:
                godown = False
            elif row == 0:
                godown = True
            if godown:
                row += 1
            else:
                row -= 1
        return ''.join(arr)

if __name__ == '__main__':
    s = Solution()
    st = "PAYPALISHIRING"
    print(s.convert(st, 3)) #"PAHNAPLSIIGYIR"