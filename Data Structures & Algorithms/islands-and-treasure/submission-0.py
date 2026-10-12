class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        rows = len(grid)
        colums = len(grid[0])

        queue =[]
        seen = set()

        for i in range(rows):
            for j in range(colums):
                if grid[i][j] == 0:
                    queue.append((i, j))
        
        while queue:
            a, b = queue.pop(0)

            if (a, b) in seen:
                continue

            seen.add((a, b))
            
            adjs = [(a+1,b), (a-1,b), (a,b+1), (a,b-1)]

            for c, d in adjs:
                if 0 <= c < rows and 0 <= d < colums:
                    if grid[c][d] != -1 and grid[c][d] != 0:
                        grid[c][d] = min(grid[c][d], grid[a][b] + 1)
                        queue.append((c, d))


        