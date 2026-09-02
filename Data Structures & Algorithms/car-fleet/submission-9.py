class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pairs = list(zip(position, speed))
        pairs.sort(reverse=True)

        for p, s in pairs:
            time = (target - p) / s
            stack.append(time)
            while len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)


    """
    zip and sort by position, 
    
    then calculate the time for each and append to stack,
    when we have two time values check if they overlap and pop
    """