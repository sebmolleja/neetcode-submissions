class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r = 0, 0
        result = []
        q = collections.deque()

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()
            
            if (r - l + 1) >= k:
                result.append(nums[q[0]])
                l += 1
            
            r += 1
        
        return result


    """
    [1,2,1,0,4,2,6]
     l
     r

    q = [1]

    compare nums when i is bigger then top of q pop
    iterate through q and append index

    check left bound and pop left when its out of bound
    if l > q[0]

    last check is adding to our result
    if (r - l) + 1 <= k
        append from left of q (biggest values)
        l += 1
    
    r += 1




    """
        