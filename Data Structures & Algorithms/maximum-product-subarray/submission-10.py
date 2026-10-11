class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        n = len(nums)
        maxprod = nums[0]
        minprod = nums[0]
        res = nums[0]

        for i in range(1, n):
            tempMax = max(nums[i], maxprod * nums[i], nums[i] * minprod)

            minprod = min(nums[i], maxprod * nums[i], nums[i] * minprod)
            maxprod = tempMax

            res = max(res, maxprod)
        
        return res

        