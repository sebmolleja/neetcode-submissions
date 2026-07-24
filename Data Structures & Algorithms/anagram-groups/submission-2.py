class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            grouped[tuple(count)].append(s)
        
        return list(grouped.values())



    """
    every single word gets array of [0] * 26:
    count [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ....]

    each character gets increment to the index of the letter 
    using the ord of the char 


    strs = ["act","pots","tops","cat","stop","hat"]

    opst

    grouped
    act : [act]
    opst: [pots]
    

    """