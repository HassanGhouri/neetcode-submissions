class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort() # .sort() is O(n)

        if nums == []:
            return 0

        max_seq = 0
        curr_seq = 1
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] > 1:
                if curr_seq > max_seq:
                    max_seq = curr_seq
                
                curr_seq = 1 
            
            elif nums[i] - nums[i-1] == 1:
                curr_seq += 1
        
        if curr_seq > max_seq:
            max_seq = curr_seq
            
        return max_seq