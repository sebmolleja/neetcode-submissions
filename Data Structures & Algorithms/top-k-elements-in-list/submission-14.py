class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        count = {}
        bucket = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        for num, freq in count.items():
            bucket[freq].append(num)
        
        for i in range(len(bucket) - 1, -1, -1):
            for num in bucket[i]:
                result.append(num)
            
            if len(result) == k:
                return result

            
        



    """
    [1,2,2,3,3,3,3,3], k = 2
    output = [2, 3]
    
    freq = {
        1 : 1,
        2 : 3,
        3 : 4
    }

    bucket = is array of arrays where index = freq:
     0    1    2   3    4   5   6  7 
    [[], [1], [], [2], [3], [], [], []]

    in each array append the value(s)

    then iterate in reverse order of your bucket and append to result values
    in each array k times.
    """
        