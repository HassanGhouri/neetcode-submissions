class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        stack = []
        seen = set()
        m = len(grid)
        n = len(grid[0])
        count = 0

        found = False
        while not found:
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1:
                        stack.append((i,j))
                        found = True
        

        while stack:
            i, j = stack.pop()
            if (i,j) not in seen:
                seen.add((i,j))
            
            else:
                continue

            surronding = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]

            for a, b in surronding:
                if a < 0 or a >= m:
                    count += 1
                
                if b < 0 or b >= n:
                    count += 1
                
                if 0 <= a < m and 0 <= b < n:
                    if grid[a][b] == 1:
                        stack.append((a,b))

                    if grid[a][b] == 0:
                        count += 1
        
        return count

        