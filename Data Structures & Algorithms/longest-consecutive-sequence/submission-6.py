class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        res = 0

        for num in nums:
            if (num - 1) not in nums_set:
                seq = 1
                curr = num
                while (curr + 1) in nums_set:
                    curr += 1
                    seq += 1
                res = max(res, seq)

        return res

    """
    nums_set = [2,20,4,10,3,4,5]
                ^

    seq = 4
    curr = 5


    """