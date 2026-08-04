class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums) 
        postfix = [1] * len(nums) 

        curr_pre, curr_post = 1, 1

        for i in range(len(nums)):
            prefix[i] = curr_pre
            curr_pre *= nums[i]

        for i in range(len(nums) - 1, -1, -1):
            postfix[i] = curr_post
            curr_post *= nums[i]

        for i in range(len(postfix)):
            prefix[i] *= postfix[i]

        return prefix

