class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pairs = sorted(list(zip(position, speed)), reverse=True)

        for p, s in pairs:
            time = (target - p) / s
            stack.append(time)

            while len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)

    """
    create pos speed list as pair # pos, speed

    sort them by position in reverse

    1, 3
    4, 2

    iterate over them, get the time it takes for them to reach target
    add to stack the time
    when there are two times in the stack check if top is bigger than
    second most top which means seperates fleets then you can pop
    """