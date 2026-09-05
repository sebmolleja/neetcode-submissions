class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        q = collections.deque() # index 
        l, r = 0, 0

        while r < len(nums):
            # pop smaller values from q
            while q and nums[q[-1]] < nums[r]:
                q.pop()  
            q.append(r)

            # update fixed window
            if l > q[0]:
                q.popleft()

            # ensure window is at least size k
            if (r + 1) >= k:
                result.append(nums[q[0]])
                l += 1
            
            r += 1
        
        
        return result


        """
        [1,2,1,0,4,2,6], k = 3
         ^
         ^

        check if no smaller values are in queue

        deque = [1, ]


        """