class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        if k == 0:
            return False

        right = k
        window = []

        for i in range(k):
            if nums[i] in window:
                return True

            window.append(nums[i])

        
        while right < len(nums):
            if nums[right] in window:
                return True
            
            else:
                window[right % k] = nums[right]
                right += 1
        
        return False

                

        