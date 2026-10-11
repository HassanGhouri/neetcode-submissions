class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Strategy, a + b + c = 0 -> a + b + -c, we fix -c and look for
        # a and b

        nums.sort()
        ans = []

        for i in range(len(nums)):
            neg_c = 0 - nums[i]

            if i > 0 and nums[i] == nums[i-1]:
                continue

            left = i + 1
            right = len(nums)-1

            while left < right:

                if nums[left] + nums[right] == neg_c:
                    ans.append([nums[left], nums[i], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                
                elif nums[left] + nums[right] <= neg_c:
                    left += 1
                
                else:
                    right -= 1
                
        
        return ans


        