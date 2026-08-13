class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, longest = 0, 0
        freq = {}

        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1

            while r - l + 1 - max(freq.values()) > k:
                freq[s[l]] -= 1
                l += 1
            
            longest = max(longest, r - l + 1)

        return longest

        """
        A A A B A B B
        ^
              ^

        window - max(values of map)

        map:
        A : 3 


        """
