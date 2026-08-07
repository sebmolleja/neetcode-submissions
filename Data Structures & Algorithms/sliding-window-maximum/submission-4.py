class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        window_max = []
        l = 0

        for r in range(len(nums)):
            freq[nums[r]] = freq.get(nums[r], 0) + 1
            while r - l + 1 == k:
                window_max.append(max(freq.keys()))
                freq[nums[l]] -= 1
                if freq[nums[l]] == 0:
                    del freq[nums[l]]
                l += 1

        return window_max

    """

    
    k = 3
    [1,2,1,0,4,2,6]
     l
         r

     check if r in set

     while r - l + 1 == k

    freq {
        1 : 2
        2 : 1

    }
    window_max = [2,

    """
