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
    longest pattern in while invalid
    use a map to track freq then delete when not needed

    X Y Y X 
    l
    r

    while window size - max(freq.values()) > k

    freq {
    X : 1
    Y : 1
    }

    """