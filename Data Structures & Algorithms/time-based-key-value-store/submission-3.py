class TimeMap:

    def __init__(self):
        self.key_values = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_values[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        values = self.key_values[key]
        l, r = 0, len(values) - 1
        timestamp_prev = ""

        while l <= r:
            mid = (l + r) // 2

            if values[mid][1] <= timestamp:
                timestamp_prev = values[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        
        return timestamp_prev