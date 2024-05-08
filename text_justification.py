from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        line = []
        line_length = 0

        for word in words:
            if line_length + len(word) + len(line) > maxWidth:
                for i in range(maxWidth - line_length):
                    line[i % (len(line) - 1 or 1)] += ' '
                ans.append(''.join(line))
                line = []
                line_length = 0
            line.append(word)
            line_length += len(word)
        return ans + [' '.join(line).ljust(maxWidth)]
        
            

if __name__ == '__main__':
    s = Solution()
    words = ["What","must","be","acknowledgment","shall","be"]
    print(s.fullJustify(words, 16))