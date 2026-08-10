class Solution:
    def encode(self, strs: List[str]) -> str: 
        encoded_string = ""

        for s in strs:
            encoded_string += str(len(s)) + '#' + s

        return encoded_string

    def decode(self, encoded_string: str) -> list[str]:
        ret = []
        i = 0

        while i < len(encoded_string):
            j = i + 1
            while encoded_string[j] != '#':
                j += 1
            curr_len = int(encoded_string[i:j])
            ret.append(encoded_string[j + 1: j + 1 + curr_len])
            i = j + 1 + curr_len
        
        return ret
      

    



    """
    5#Hello5#World
    ij



    """
         

