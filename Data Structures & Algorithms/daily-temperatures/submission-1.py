class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # [temperature, index] pair
        ret = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                stack_temp, stack_index = stack.pop()
                ret[stack_index] = i - stack_index
            stack.append([t, i])
        
        return ret

    """
    [30, 38, 30, 36, 35, 40, 28]
                         ^

    stack = [38]
    result = [1, ]

    append count (1), pop, append 
    append count (4), pop, append curr


    

    

     """