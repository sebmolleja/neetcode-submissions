class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        k = r

        while l <= r:
            mid = (l + r) // 2

            time = 0
            for p in piles:
                time += math.ceil(p / mid)

            if time <= h:
                k = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return k


    """
    [1,4,3,2], h = 9
     ^

     max value of piles = 4 so speed = 1 - 4
     mid = 2

    total_time += piles[i] // k
    if <= h:
        result = k # can we go lower ?
        r = k - 1
    else:
        l = k + 1
     


    """