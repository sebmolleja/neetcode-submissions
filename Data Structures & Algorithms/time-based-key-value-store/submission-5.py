class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        values = self.timemap[key]
        timestamp_prev = ""

        l, r = 0, len(values) - 1
        while l <= r:
            mid = (l + r) // 2

            if timestamp >= values[mid][1]:
                timestamp_prev = values[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        
        return timestamp_prev

        

    """
    timemap = { 
                    0           1        2           3
        alice : [(happy, 1), (sad, 3), (angry, 5), (bored, 7)]
                                                        l
                                                         r
                                                         ^

                    6 >= 3, timestamp_prev = sad
                    6 >= 5 timestamp_prev = angry
                    6 >= 7

    }





    """