from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        min_k = right


        while left <= right:

            cannidate_k = (left + right) // 2
            total_hours = 0

            for pile in piles:
                total_hours += ceil(pile/cannidate_k)
            
            if total_hours <= h:
                min_k = cannidate_k
                right = cannidate_k - 1

            else:
                left = cannidate_k + 1
        
        return min_k






        
        