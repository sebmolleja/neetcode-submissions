class Solution:
    def trap(self, height: List[int]) -> int:
      l, r = 0, len(height) - 1
      leftMax, rightMax = height[l], height[r]
      area = 0

      while l < r:
        if leftMax < rightMax:
          l += 1
          leftMax = max(leftMax, height[l])
          area += leftMax - height[l]
        else:
          r -= 1
          rightMax = max(rightMax, height[r])
          area += rightMax - height[r]

      return area

    """
    [0,2,0,3,1,0,1,3,2,1]
           l 
             r

    leftMax = 0, 2, 3
    rightMax = 1, 2, 3
    area = 2, 4, 7, 9
    

    """