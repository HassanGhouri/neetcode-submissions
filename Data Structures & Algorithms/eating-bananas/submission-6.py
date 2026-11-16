from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left = 1
        right = max(piles)
        min_k = max(piles)

        while left <= right:
            k = (left + right) // 2
            total_t = 0
            print(min_k, k)

            for pile in piles:
                total_t += ceil(pile / k)
            
            if total_t <= h:
                min_k = min(min_k, k)
                right = k - 1
            
            else:
                left = k + 1
                
        
        return min_k


        