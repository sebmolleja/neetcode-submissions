class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        for s in strs:
            result += str(len(s)) + '#' + s
        
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        j = 0

        while j < len(s):
            i = j
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            result.append(s[j + 1:j + 1 + length])
            j = j + 1 + length

        return result

    """
    strs = ["Hello","World"]

    encode: 
    5#Hello5#World

    decode:
    5#Hello5#World
    i
    j

    
     



    """
