class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        colums = len(grid[0])

        ans = 0
        seen = set()

        for i in range(rows):
            for j in range(colums):
                count = 0

                if grid[i][j] == 0:
                    seen.add((i, j))
                
                elif grid[i][j] not in seen:
                    stack = [(i, j)]

                    while stack:
                        a,b = stack.pop()

                        if (a,b) in seen or grid[a][b] == 0:
                            continue
                        
                        seen.add((a,b))
                        count += 1
                        adjs = [(a-1, b),(a+1, b),(a, b-1),(a,b + 1)]

                        for adj in adjs:
                            c, d = adj

                            if 0 <= c <= rows-1 and 0 <= d <= colums-1 and (c, d) not in seen and (c,d) not in stack:
                                stack.append((c, d))

                    ans = max(ans, count)
        
        return ans




        