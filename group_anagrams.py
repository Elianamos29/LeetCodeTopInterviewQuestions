from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_g = {}
        
        for i in range(len(strs)):
            sorted_str = "".join(sorted(strs[i]))
            if sorted_str not in hash_g:
                hash_g[sorted_str] = [strs[i]]
            else:
                hash_g[sorted_str].append(strs[i])
        return hash_g.values()

if __name__ == '__main__':
    s = Solution()
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(s.groupAnagrams(strs)) # [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
    strs = [""]
    print(s.groupAnagrams(strs)) # [[""]]
    strs = ["a"]
    print(s.groupAnagrams(strs)) # [["a"]]