class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        compliments = {}
        n = len(nums)

        for i in range(n):
            if nums[i] in compliments:
                return sorted([i, compliments[nums[i]]])
            
            else:
                compliments[target - nums[i]] = i
        
        