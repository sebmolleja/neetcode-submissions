class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        area, most_water = 0, 0

        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            most_water = max(most_water, area)

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        
        return most_water


    """
    height = [1,7,2,5,4,7,3,6]
              l
                            r
    area = min(height[l], height[r]) * r - l
    area = 7, 36, 



    """