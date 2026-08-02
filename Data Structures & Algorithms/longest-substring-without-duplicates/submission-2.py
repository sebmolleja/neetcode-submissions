class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest, l, r = 0, 0, 0
        seen = set()

        while r < len(s):
            if s[r] in seen:
                seen.remove(s[l])
                l += 1
            else:
                seen.add(s[r])
                longest = max(longest, (r - l + 1))
                r += 1
        
        return longest


    """
    "pwwkew"
     ^
       ^

    seen = {p, w}
    longest = 0


    start window 0, 0 increment and use set to track i we've seen it
    when weve already seen get max r - l 
    update l side of window by 1 
    """


  