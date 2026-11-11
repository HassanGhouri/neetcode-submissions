class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = []
        fresh = 0
        m = len(grid)
        n = len(grid[0])
        max_time = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                
                elif grid[i][j] == 2:
                    queue.append([(i, j), 0])
        
        head = 0
        while head < len(queue):
            cell, time = queue[head]
            a, b = cell
            max_time = max(max_time, time)
            head += 1

            adjs = [(a+1, b), (a-1, b), (a, b+1), (a, b-1)]

            for c, d in adjs:
                if 0 <= c < m and 0 <= d < n:
                    if grid[c][d] == 1:
                        grid[c][d] = 2
                        queue.append([(c,d), time + 1])
                        fresh -= 1
            
        if fresh != 0:
            return -1

        return max_time


        
        