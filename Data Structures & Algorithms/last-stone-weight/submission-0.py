import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)

        while len(heap) > 1:
            x = -heapq.heappop(heap)
            y = -heapq.heappop(heap)

            if x != y:
                new = max(x, y) - min(x,y)
                heapq.heappush(heap, -new)
        
        if len(heap) == 0:
            return 0
        
        return -heap[0]



        