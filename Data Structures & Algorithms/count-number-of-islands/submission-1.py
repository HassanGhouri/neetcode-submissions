class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        seen = set()
        stack = []
        count = 0


        for i in range(m):
            for j in range(n):

                if grid[i][j] == "1" and (i,j) not in seen:
                    count += 1
                    stack.append((i,j))

                    while stack:
                        a, b = stack.pop()
                        seen.add((a,b))

                        adjs = [(a+1,b), (a-1,b), (a,b-1), (a,b+1)]

                        for c, d in adjs:
                            if 0 <= c < m and 0 <= d < n:
                                if grid[c][d] == "1":
                                    if (c,d) not in seen:
                                        stack.append((c,d))

        return count 

        