class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        seen = set()
        stack = []
        max_island = 0
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i,j) not in seen:
                    count = 0
                    stack.append((i,j))
                    seen.add((i,j))

                    while stack:
                        a, b = stack.pop()
                        count += 1
                        
                        adjs = [(a+1,b), (a-1,b), (a,b+1), (a,b-1)]

                        for c, d in adjs:
                            if 0 <= c < m and 0 <= d < n:
                                if (c,d) not in seen and grid[c][d] == 1:
                                    stack.append((c, d))
                                    seen.add((c,d))
                    
                    max_island = max(max_island, count)

        
        return max_island

        