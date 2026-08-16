class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        freq_s1, freq_s2 = {}, {}

        for char in s1: 
            freq_s1[char] = freq_s1.get(char, 0) + 1

        for r in range(len(s2)):
            freq_s2[s2[r]] = freq_s2.get(s2[r], 0) + 1

            while r - l + 1 == len(s1):
                if freq_s1 == freq_s2:
                    return True
                
                freq_s2[s2[l]] -= 1
                if freq_s2[s2[l]] == 0:
                    del freq_s2[s2[l]]

                l += 1

        return False


        """
        l e c a b e e
          ^
              ^

        a : 1
        b : 1
        c : 1

        e : 1
        c : 1
       

        """