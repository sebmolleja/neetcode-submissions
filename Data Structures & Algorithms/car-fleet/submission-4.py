class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pairs = list(zip(position, speed)) # pos, speed

        pairs.sort(reverse=True)

        for p, s in pairs:
            time = (target - p) / s
            stack.append(time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)


    """
    target = 10
    pos = [1, 4]
    speed = [3, 2]

    (1, 3), (4, 2)

    time = 10 - 1 / 3 = 3
    time = 10 - 4 / 2 = 3

    stack = [3, 3]
    """