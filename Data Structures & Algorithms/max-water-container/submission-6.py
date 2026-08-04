class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        ret, area = 0, 0

        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            ret = max(ret, area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return ret

    """
    area = min of heights and the difference between them
    choose what to increment based on which is less 


    [1,7,2,5,4,7,3,6]
       l           r

     area = 6
    """