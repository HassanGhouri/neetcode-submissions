class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        max_time = 0
        rows = len(grid)
        colums = len(grid[0])

        fresh = 0
        queue = []

        for i in range(rows):
            for j in range(colums):
                time = 0

                if grid[i][j] == 2:
                    queue.append((i, j, 0))
                
                elif grid[i][j] == 1:
                    fresh += 1
        
        while queue:
            a, b, time = queue.pop(0)

            adjs = [(a+1,b),(a-1,b),(a,b+1),(a,b-1)]

            for c, d in adjs:
                if 0<=c<rows and 0<=d<colums:
                    if grid[c][d] == 1:
                        grid[c][d] = 2

                        fresh-=1

                        queue.append((c, d, time+1))
                        max_time = max(max_time, time+1)

        if fresh != 0:
            return -1

        
        return max_time

        