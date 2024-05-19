from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count
        word_dict = {}
        for word in words:
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1
        result = []
        for i in range(len(s) - total_len + 1):
            temp_dict = {}
            j = 0
            while j < word_count:
                word = s[i + j * word_len: i + (j + 1) * word_len]
                if word not in word_dict:
                    break
                if word in temp_dict:
                    temp_dict[word] += 1
                else:
                    temp_dict[word] = 1
                if temp_dict[word] > word_dict[word]:
                    break
                j += 1
            if j == word_count:
                result.append(i)
        return result

if __name__ == '__main__':
    s = "barfoothefoobarman"
    words = ["foo", "bar"]
    solution = Solution()
    print(solution.findSubstring(s, words))
                
            
            