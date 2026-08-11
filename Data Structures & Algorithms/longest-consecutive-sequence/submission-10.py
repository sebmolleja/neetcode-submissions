class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0

        for num in nums:
            if num - 1 not in nums_set:
                seq = 1
                curr = num
                while curr + 1 in nums_set:
                    seq += 1
                    curr += 1
                longest = max(longest, seq)
        
        return longest

    """
    use set for nums
    if nums - 1 not in there we start it

    [2,20,4,10,3,4,5]
     

    """