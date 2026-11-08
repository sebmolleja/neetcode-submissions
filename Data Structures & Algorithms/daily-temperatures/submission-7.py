class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # (index, temp)
        result = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                stack_index, stack_temp = stack.pop()
                result[stack_index] = i - stack_index 
            stack.append((i, temp))
        
        return result

