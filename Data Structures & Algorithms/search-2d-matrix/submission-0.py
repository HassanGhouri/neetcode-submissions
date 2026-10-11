class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        left = 0
        right = m-1
        row = -1

        while left <= right:
            mid = (left + right) // 2

            if matrix[mid][0] <= target <= matrix[mid][n-1]:
                row = mid
                break
            
            else:
                if target < matrix[mid][0]:
                    right = mid - 1

                else:
                    left = mid + 1
        
        left = 0
        right = n-1

        while left <= right:
            mid = (left + right) // 2

            if matrix[row][mid] == target:
                return True
            
            else:
                if target < matrix[row][mid]:
                    right = mid - 1

                else:
                    left = mid + 1
        
        return False

        