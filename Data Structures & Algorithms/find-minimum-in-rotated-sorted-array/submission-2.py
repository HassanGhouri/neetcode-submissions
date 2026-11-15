class Solution:
    def findMin(self, nums: List[int]) -> int:

        min_num = float('inf')
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[left] <= nums[mid]:  # left sorted
                min_num = min(min_num, nums[left])
                left = mid + 1

            
            elif nums[mid] <= nums[right]:
                min_num = min(min_num, nums[mid])
                right = mid -1
            
        return min_num


        