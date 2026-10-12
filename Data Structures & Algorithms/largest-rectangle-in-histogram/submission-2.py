class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = [] # (index, height)
        max_area = 0

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                stack_index, stack_height = stack.pop() 
                max_area = max(max_area, (i - stack_index) * stack_height)
                start = stack_index
            stack.append((start, h))

        for i, h in stack:
            max_area = max(max_area, (len(heights) - i) * h)
        
        return max_area
 