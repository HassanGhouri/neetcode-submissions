class Solution:
    def findMin(self, nums: List[int]) -> int:

        min_val = float('inf')
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            min_val = min(min_val, nums[mid])

            if nums[left] <= nums[mid]:
                # Left sorted
                 min_val = min(min_val, nums[left])
                 left = mid + 1
                
            else:
                #right sorted
                right = mid - 1
        
        return min_val

        