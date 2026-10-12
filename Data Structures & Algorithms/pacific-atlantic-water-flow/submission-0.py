class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        ans = []
        rows = len(heights)
        colums = len(heights[0])

        pacific = set()
        atlantic = set()
        pacific_stack = []
        atlantic_stack = []
        
        for i in range(colums):
            pacific_stack.append((0, i))

        for i in range(1, rows):
            pacific_stack.append((i, 0))

        for i in range(colums):
            atlantic_stack.append((rows-1, i))
        
        for i in range(rows-1):
            atlantic_stack.append((i, colums-1))
        
        
        while pacific_stack:
            a, b = pacific_stack.pop()

            if (a, b) in pacific:
                continue

            pacific.add((a, b))

            for c, d in [(a-1, b), (a+1, b), (a, b-1), (a, b+1)]:
                if 0 <= c < rows and 0 <= d < colums:
                    if (c, d) not in pacific and heights[c][d] >= heights[a][b]:
                        pacific_stack.append((c,d))
        
        while atlantic_stack:
            a, b = atlantic_stack.pop()

            if (a, b) in atlantic:
                continue

            atlantic.add((a, b))

            for c, d in [(a-1, b), (a+1, b), (a, b-1), (a, b+1)]:
                if 0 <= c < rows and 0 <= d < colums:
                    if (c, d) not in atlantic and heights[c][d] >= heights[a][b]:
                        atlantic_stack.append((c,d))
            


        for coord in pacific:
            if coord in atlantic:
                a, b = coord
                ans.append([a, b])

        return ans
            


        

        

