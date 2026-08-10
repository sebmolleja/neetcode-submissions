class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq, ret = {}, []
        bucket = [[] for _ in range(len(nums) + 1)]

        for char in nums:
            freq[char] = freq.get(char, 0) + 1
        
        for num, count in freq.items():
            bucket[count].append(num)
        
        for i in range(len(bucket) - 1, -1, -1):
            for num in bucket[i]:
                ret.append(num)

                if len(ret) == k:
                    return ret
        
        return

    """
    count with freq map
    use bucket with arrays of arrays 
    index of that bucket is the freq

    
    """