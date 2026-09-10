class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        bucket = [[] for _ in range(len(nums) + 1)]
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        for num, count in freq.items():
            bucket[count].append(num)

        for i in range(len(bucket) - 1, -1, -1):
            for num in bucket[i]:
                result.append(num)

            if len(result) == k:
                return result
        
         


    """
    [1,2,2,3,3,3,3], k = 2

    freq = {
    1 : 1
    2 : 2
    3:  4
    }


    bucket = [[], [], [], [] ] # where index is freq, element is the actual value

    reverse through the bucket with extra element and append to result list


    """