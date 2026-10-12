class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Strategy, iterate over the grid, add every water to seen,
        # When I encounter an Island, do DFS, add its parts to seen.

        rows = len(grid)
        colums = len(grid[0])
        seen = set()
        islands = 0

        for i in range(rows):
            for j in range(colums):

                if grid[i][j] == "0":
                    seen.add((i, j))
                
                elif (i, j) not in seen:
                    stack = [(i, j)]
                    islands += 1

                    while stack:
                        a, b = stack.pop()

                        if (a,b) in seen:
                            continue

                        if grid[a][b] == "1":
                            seen.add((a, b))

                            adjs = [(a-1, b),(a+1, b),(a, b-1),
                            (a,b + 1)]

                            for adj in adjs:
                                c, d = adj

                                if 0 <= c <= rows-1 and 0 <= d <= colums-1:
                                    if grid[c][d] == "1" and (c,d) not in seen:
                                        stack.append(adj)  

        return islands
        