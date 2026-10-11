class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Fix first value, use two points to find second value

        ans = []

        nums.sort()
        n = len(nums)

        for i in range(n-1):
            neg_a = 0-nums[i]

            left = i+1
            right = n-1

            if i > 0 and nums[i] == nums[i-1]:
                continue

            while left < right:
                if nums[left] + nums[right] == neg_a:
                    ans.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                
                elif nums[left] + nums[right] < neg_a:
                    left += 1
                
                else:
                    right -= 1
            
        return ans
