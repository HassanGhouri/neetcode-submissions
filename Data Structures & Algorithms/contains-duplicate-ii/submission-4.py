class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        if k == 0:
            return False

        left = 0
        right = k
        window = set()

        for i in range(k):
            if nums[i] in window:
                return True

            window.add(nums[i])

        
        while right < len(nums):
            if nums[right] in window:
                return True
            
            else:
                window.remove(nums[left])
                window.add(nums[right])
                right += 1
                left += 1
        
        return False

                

        