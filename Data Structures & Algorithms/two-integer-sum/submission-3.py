class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = {}

        for i, num in enumerate(nums):
            difference = target - num
            if difference in check:
                return [check[difference], i]
            check[num] = i
        
        return 



    """

    [3, 4, 5, 6], target = 7
        ^

    check = {
        3 : 0

    }


    """
