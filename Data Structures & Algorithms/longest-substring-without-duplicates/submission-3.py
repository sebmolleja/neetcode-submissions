class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest, l = 0, 0
        seen = set()

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            longest = max(longest, r - l + 1)

        return longest

    """
    "pwwkew"
        ^
          ^

    seen = {k, e}
    longest = 3


    start window 0, 0 increment and use set to track i we've seen it
    when weve already seen get max r - l 
    update l side of window by 1 
    """


  