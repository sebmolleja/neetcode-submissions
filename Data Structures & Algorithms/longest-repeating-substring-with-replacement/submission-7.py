class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest, l = 0, 0
        freq = {}

        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1

            while r - l + 1 - max(freq.values()) > k:
                freq[s[l]] -= 1
                l += 1
            
            longest = max(longest, r - l + 1)

        return longest
                

    """
    k = 2

    A A A B A B B
      l
              r

    map:
    A : 4
    B: 1

    k = 1, 


    if s[r] not in my map AND k > 0 then 
        decrement k increment
        walk r
    else its in my map so
        keep r += 1
        get max here ? need it to be in else? 

    """