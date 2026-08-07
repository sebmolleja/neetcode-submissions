class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l, shortest = 0, float('inf')
        s_freq, t_freq = {}, {}

        for char in t:
            t_freq[char] = t_freq.get(char, 0) + 1

        have, need = 0, len(t_freq)

        for r in range(len(s)):
            if s[r] in t_freq:
                s_freq[s[r]] = s_freq.get(s[r], 0) + 1
                if s_freq[s[r]] == t_freq[s[r]]:
                    have += 1
            
            while have == need:
                if r - l + 1 < shortest:
                    minSubstring = s[l:r + 1]
                    shortest = min(shortest, r - l + 1)
                
                if s[l] in t_freq:
                    s_freq[s[l]] -= 1
                    if s_freq[s[l]] < t_freq[s[l]]:
                        have -= 1
                
                l += 1


        return minSubstring if shortest != float('inf') else ""
            


    """
    "OUZODYXAZV", t = "XYZ"

    O U Z O D Y X A Z V
    l
      r

    x : 1
    y : 1
    z : 1

    have = 0
    need = 0





    """