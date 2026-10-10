class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, longest = 0, 0
        seen = set()

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            longest = max(longest, r - l + 1) 
        
        return longest
    

    """

    zxyzxyz
     ^
       ^

   seen = {x, y, z}
   longest = 1, 2, 3



    """

        