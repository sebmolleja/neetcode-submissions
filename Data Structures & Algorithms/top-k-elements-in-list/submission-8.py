class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ret, count = [], {}
        bucket = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            count[num] = count.get(num, 0) + 1

        for num, freq in count.items():
            bucket[freq].append(num)
        
        for i in range(len(bucket) - 1, -1, -1):
            for num in bucket[i]:
                ret.append(num)
            if len(ret) == k:
                return ret


    
    """
    nums = [1,2,2,3,3,3,3], k = 2

    count =
    1 : 1
    2 : 2
    3 : 4
              0    1    2   3     4   5    6   7
    bucket = [[], [1], [2], [],  [3], [3], []  []  ]


    """
