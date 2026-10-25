class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        times = list(zip(position, speed))
        times.sort(reverse=True)

        for p, s in times:
            time = (target - p) / s
            stack.append(time)
            while len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)


    """
    target = 10, position = [4,1,0,7], speed = [2,2,1,1]

    time formula is (target - p) / speed

    position=[1,4] speed=[3,2]

    (4, 2)
    (1, 3)

    [3, 3]





    """

        