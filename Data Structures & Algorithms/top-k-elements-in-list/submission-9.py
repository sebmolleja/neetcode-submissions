class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ret, freq = [], {}
        bucket = [[] for _ in range(len(nums) + 1)]

        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        
        for num, count in freq.items():
            bucket[count].append(num)
        
        for i in range(len(bucket) - 1, -1, -1):
            for num in bucket[i]:
                ret.append(num)

                if len(ret) == k:
                    return ret


    """
    nums = [1,1,1,2,2,3,3,3,3], k = 2

    bucket = [[], [], [2], [1], [3] etc..]

    freq:
    1: 3
    2: 2
    3: 4

    items(): 3, 2, 4

    
    """