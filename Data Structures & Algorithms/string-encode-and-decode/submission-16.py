class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""

        for s in strs:
            encoded_string += str(len(s)) + '#' + s

        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_string = []
        i = 0

        while i < len(s):
            j = i + 1
            while s[j] != '#':
                j += 1
            curr_len = int(s[i:j])
            decoded_string.append(s[j + 1: j + 1 + curr_len])
            i = j + 1 + curr_len
        
        return decoded_string


    """
    ["Hello","World"]

    5#Hello5#World
    i
     j


    """