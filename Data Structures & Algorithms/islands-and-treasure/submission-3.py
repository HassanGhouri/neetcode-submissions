class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        m = len(grid)
        n = len(grid[0])
        queue = []

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    queue.append((i,j))
        
        head = 0
        while head < len(queue):
            a, b = queue[head]
            head += 1

            adjs = [(a+1,b),(a-1,b),(a,b+1),(a,b-1)]

            for c,d in adjs:
                if 0 <= c < m and 0 <= d < n:
                    if grid[c][d] == 2147483647:
                        grid[c][d] = grid[a][b] + 1
                        queue.append((c,d))
        


        