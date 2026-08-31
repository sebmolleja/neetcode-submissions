class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        longest = 0

        for num in nums:
            if num - 1 not in seen:
                seq = 1
                curr = num
                while curr + 1 in seen:
                    seq += 1
                    curr += 1
                longest = max(longest, seq)

        return longest


    """
    nums = [2,20,4,10,3,4,5]

    use set to check 


    """