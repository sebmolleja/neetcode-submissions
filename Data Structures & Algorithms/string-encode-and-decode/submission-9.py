class Solution:
    def encode(self, strs: List[str]) -> str: 
        ret = ""
        for s in strs:
            ret += str(len(s)) + '#' + s

        return ret

    def decode(self, encoded_string: str) -> list[str]:
        ret = []
        i = 0

        while i < len(encoded_string):
            j = i
            while encoded_string[j] != "#":
                j += 1
            curr_len = int(encoded_string[i:j])
            ret.append(encoded_string[j + 1: j + 1 + curr_len])
            i = j + 1 + curr_len
    
        return ret



    """
     strs = ["Hello","World"]

     ret = 5#Hello5#World

     curr_len_str = 5
     # + 1 = start of word
     ret = curr_len_str (string slice it)
    
    """
         

