import heapq
from math import sqrt
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap = []
        x1 = 0
        y1 = 0

        for point in points:
            x2, y2 = point
            distance = (sqrt(((x1 - x2) ** 2) + ((y1 - y2) **2)))

            heapq.heappush(heap, (distance, [x2, y2]))
        
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(heap)[1])

        return ans
        