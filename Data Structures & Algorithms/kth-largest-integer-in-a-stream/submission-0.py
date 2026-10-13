import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
        
        for num in nums:
            heapq.heappush(self.heap, -num)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, -val)
        temp = []

        for i in range(self.k):
            temp.append(heapq.heappop(self.heap))
        
        ans = -temp[-1]

        for num in temp:
            heapq.heappush(self.heap, num)
        
        return ans
        


        
