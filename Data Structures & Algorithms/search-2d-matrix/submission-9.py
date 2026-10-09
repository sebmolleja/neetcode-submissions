class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        l, r = 0, ROWS - 1
        while l <= r:
            mid = (l + r) // 2

            if target > matrix[mid][COLS - 1]:
                l = mid + 1
            elif target < matrix[mid][0]:
                r = mid - 1
            else:
                break

        row = mid
        l, r = 0, COLS - 1

        while l <= r:
            mid = (l + r) // 2

            if target > matrix[row][mid]:
                l = mid + 1
            elif target < matrix[row][mid]:
                r = mid - 1
            else:
                return True

        return False
        

    

    """


       0          1               2
    [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10




    """
        