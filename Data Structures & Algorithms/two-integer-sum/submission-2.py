class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement = {}

        for index, num in enumerate(nums):
            diff = target - num
            if diff in complement:
                return [complement[diff], index]
            complement[num] = index

        return


        """
        [4, 5, 6], target = 10
               ^

        diff = 10 - num

        4 : 0
        5 : 1





        """