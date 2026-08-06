class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        freq1, freq2 = {}, {}

        for s in s1:
            freq1[s] = freq1.get(s, 0) + 1

        for r in range(len(s2)):
            freq2[s2[r]] = freq2.get(s2[r], 0) + 1

            while r - l + 1 > len(s1):
                freq2[s2[l]] -= 1
                if freq2[s2[l]] == 0:
                    del freq2[s2[l]]
                l += 1
            
            if freq1 == freq2:
                return True
        
        return False

    """
    get freq of s1
    
    s2 window over the length of s1 untill the freqs is the same as s1 return True
    """