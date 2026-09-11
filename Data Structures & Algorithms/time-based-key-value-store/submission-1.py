class TimeMap:

    def __init__(self):
        self.time_stamp = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_stamp[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        timestamps = self.time_stamp[key]
        l, r  = 0, len(timestamps) - 1
        timestamp_prev = ""

        while l <= r:
            mid = (l + r) // 2

            if timestamps[mid][1] <= timestamp:
                timestamp_prev = timestamps[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        
        return timestamp_prev

    """

    TimeStamp = { 0          1          2
        alice : [(happy, 1), (sad, 3), (angry, 6)]
    }


    """