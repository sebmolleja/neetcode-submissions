class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        shortest = float('inf')
        freq_s, freq_t = {}, {}
        min_substring = ""

        for char in t:
            freq_t[char] = freq_t.get(char, 0) + 1
        
        have, need = 0, len(freq_t)
        
        for r in range(len(s)):
            if s[r] in freq_t:
                freq_s[s[r]] = freq_s.get(s[r], 0) + 1
                if freq_s[s[r]] == freq_t[s[r]]:
                    have += 1

            while have == need:
                if r - l + 1 < shortest:
                    shortest = min(shortest, r - l + 1)
                    min_substring = s[l:r + 1]
                
                if s[l] in freq_t:
                    freq_s[s[l]] -= 1
                    if freq_s[s[l]] < freq_t[s[l]]:
                        have -= 1
                l += 1
        
        return min_substring if shortest != float('inf') else ""


    """
    pattern for shortest so in while loop valid
    use have and need calc to know what chars are the same in both freq maps

    update have before while after update s map and have

    O U Z O D Y X A Z V
        l
                r

    x : 1   x : 1
    y : 1   y : 1
    z : 1   z : 1

    have = 0
    need = 3


    """