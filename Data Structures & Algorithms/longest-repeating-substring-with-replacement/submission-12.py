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
    longest window pattern
    outside of while loop where condition is broken

    use freq map to count delete the key entirely when
    out of map? 

    while window size - max value in map > K 

    AAABABB
         ^

    A: 3
    B: 1

    """
        