class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        res = 0

        for num in nums_set:
            if num - 1 not in nums_set:
                seq = 1
                curr = num
                while curr + 1 in nums_set:
                    seq += 1
                    curr += 1
                res = max(res, seq)

        return res


    """
    [2,20,4,10,3,4,5]

    start seq when num - 1 not in set and check increment each time then get max 

    """