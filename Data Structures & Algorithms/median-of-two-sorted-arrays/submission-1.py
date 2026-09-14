class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2
            j = half - i - 2

            Aleft = A[i] if i >= 0 else float("-inf")
            Aright = A[i + 1] if (i + 1) < len(A) else float("inf")
            Bleft = B[j] if j >= 0 else float("-inf")
            Bright = B[j + 1] if (j + 1) < len(B) else float("inf")

            # partition is valid
            if Aleft <= Bright and Bleft <= Aright:
                # odd number
                if total % 2:
                    return min(Aright, Bright)
                # even number
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1



    """
    perform the partition on the smaller array A always
    set l and r on smaller array A then infinite while since we'll always find an answer
    declare mid for a
    declare mid for b which is half - i - 2 to account for indexing

    then we want to find the numbers to compare to see if we found the correct partition
    that would be values Aleft which is mid and mid + 1 which is in right side of partition
    same thing with values in the other array B
    need to give default values of -inf and inf when out of bounds (too far left would be -inf) and (too far right inf)
    """
