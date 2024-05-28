class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        hash_w = {}

        for i in range(len(pattern)):
            if pattern[i] not in hash_w:
                if words[i] in hash_w.values():
                    return False
                hash_w[pattern[i]] = words[i]
            if hash_w[pattern[i]] != words[i]:
                return False
        
        return True

if __name__ == '__main__':
    s = Solution()
    print(s.wordPattern('abba', 'dog cat cat dog'))  # True
    print(s.wordPattern('abba', 'dog cat cat fish'))  # False
    print(s.wordPattern('aaaa', 'dog cat cat dog'))  # False
    print(s.wordPattern('ab', 'dog dog'))  # False