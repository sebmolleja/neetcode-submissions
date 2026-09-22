class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = list(zip(position, speed))
        pairs.sort(reverse=True)
        stack = []

        for p, s in pairs:
            time = (target - p) / s
            stack.append(time)
            while len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)

        """
        target = 10
        (4, 2)
        (1, 3)


        stack = [3] 



        """

