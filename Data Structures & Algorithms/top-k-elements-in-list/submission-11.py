class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ret, freq = [], {}
        bucket = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        for num, freq in freq.items():
            bucket[freq].append(num)

        for i in range(len(bucket) - 1, -1, -1):
            for num in bucket[i]:
                ret.append(num)

                if len(ret) == k:
                    return ret
        
        return

    """
    map to get freq
    index of map is freq, elements of each subarray are the value

    bucket = [[], [], [], [], [], []]

    """
