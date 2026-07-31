class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1 

            while l < r:
                total = nums[i] + nums[l] + nums[r]

                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    
        return res
                

    """
    [-4, -1, -1, 0, 1, 2]
          i   j        k

    [-1, -1, 2], [-1, 0, 1]

    when it is == 0 skip current i and restart

    [-1, 0, 1, 2, -1, -4]
      i  j             k

    nums[i] + nums[j] + nums[k] == 0
    ret = [[-1, 0, 1], ]


    """
