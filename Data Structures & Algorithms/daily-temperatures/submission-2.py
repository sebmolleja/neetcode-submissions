class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # temperature, index
        result = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                stack_temp, stack_index = stack.pop()
                result[stack_index] = i - stack_index
            stack.append([t, i])
        
        return result


    """
    stack = (temperature, index)
    monotonic stack using index to track order

    [30,38,30,36,35,40,28]
        ^

    stack = [(30, 0),  ]
    popped = 30, 0


    result = [0, 0, 0, 0, 0, 0, 0]
    """