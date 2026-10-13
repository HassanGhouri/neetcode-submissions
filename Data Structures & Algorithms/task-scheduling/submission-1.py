import heapq
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        count = Counter(tasks)

        heap = [-freq for freq in count.values()]
        heapq.heapify(heap)
        # heap is now a max ordered freq list

        cooldown = []
        time = 0

        while heap or cooldown:
            time += 1

            if heap:
                freq = heapq.heappop(heap) + 1

                if freq != 0:
                    cooldown.append(((time + n), freq))
            
            if cooldown and cooldown[0][0] <= time:
                ready_time, freq = cooldown.pop(0)
                heapq.heappush(heap, freq)
        
        return time
