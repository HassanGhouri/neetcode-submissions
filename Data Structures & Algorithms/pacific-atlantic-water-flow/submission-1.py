class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        pacific = set()
        atlantic = set()
        pacific_queue = []
        atlantic_queue = []
        m = len(heights)
        n = len(heights[0])

        for i in range(m):
            pacific.add((i, 0))
            pacific_queue.append((i, 0))
        
        for i in range(n):
            pacific.add((0, i))
            pacific_queue.append((0, i))

        
        for i in range(m):
            atlantic.add((i, n-1))
            atlantic_queue.append((i, n-1))
        
        for i in range(n):
            atlantic.add((m-1, i))
            atlantic_queue.append((m-1, i))

        pacific_head = 0
        while pacific_head < len(pacific_queue):
            a, b = pacific_queue[pacific_head]
            pacific_head += 1

            adjs = [(a+1,b), (a-1,b), (a,b+1), (a,b-1)]

            for c,d  in adjs:
                if 0 <= c < m and 0 <= d < n:
                    if heights[c][d] >= heights[a][b]:
                        if (c,d) not in pacific:
                            pacific.add((c,d))
                            pacific_queue.append((c,d))
        

        atlantic_head = 0
        while atlantic_head < len(atlantic_queue):
            a, b = atlantic_queue[atlantic_head]
            atlantic_head += 1

            adjs = [(a+1,b), (a-1,b), (a,b+1), (a,b-1)]

            for c,d  in adjs:
                if 0 <= c < m and 0 <= d < n:
                    if heights[c][d] >= heights[a][b]:
                        if (c,d) not in atlantic:
                            atlantic.add((c,d))
                            atlantic_queue.append((c,d))
        
        ans = []

        for elm in atlantic:
            if elm in pacific:
                r, c = elm
                ans.append([r, c])
        
        return ans
            





        