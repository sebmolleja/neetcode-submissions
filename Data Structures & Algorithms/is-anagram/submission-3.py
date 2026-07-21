class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word1map = {}
        word2map = {}
        
        for char in s:
            word1map[char] = word1map.get(char, 0) + 1

        for char in t:
            word2map[char] = word2map.get(char, 0) + 1

        return word1map == word2map