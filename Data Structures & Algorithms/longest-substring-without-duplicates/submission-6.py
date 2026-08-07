class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest, l = 0, 0
        seen = set()

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            longest = max(longest, r - l + 1)
            seen.add(s[r])

        return longest


    """
    use set in longest window pattern

    z x y z x y z
    l
          r

    {z, }


    """
