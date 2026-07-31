class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = len(nums) - 1 

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total > 0:
                    k -= 1
                elif total < 0:
                    j += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    k -= 1
                    j += 1

                    # another duplicate check here
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                    
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
