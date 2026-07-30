class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            if (numbers[l] + numbers[r]) > target:
                r -= 1
            elif (numbers[l] + numbers[r]) < target:
                l += 1
            else:
                return [l + 1, r + 1]

    """
    [1, 2, 3, 4], target = 3
     l  r

    l + r > target
        r -= 1
    l + r < target
        l += 1
    else means equal:
        return l and r 1 + index
    """