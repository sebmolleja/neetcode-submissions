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
            j = i
            while s[j] != '#':
                j += 1
            s_len = int(s[i:j])
            s_curr = s[j + 1: j + 1 + s_len]
            decoded_string.append(s_curr)
            i = j + 1 + s_len
        
        return decoded_string
