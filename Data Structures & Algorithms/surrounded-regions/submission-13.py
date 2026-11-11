class Solution:
    def solve(self, board: List[List[str]]) -> None:

        m = len(board)
        n = len(board[0])
        seen = set()

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O" and (i,j) not in seen:
                    region = [(i,j)]
                    stack = [(i, j)]
                    valid = True
                    seen.add((i, j))

                    while stack:
                        a, b = stack.pop()
                        
                        adjs = [(a+1,b), (a-1,b), (a,b+1), (a,b-1)]

                        for c, d in adjs:
                            if 0 <= c < m and 0 <= d < n:
                                if (c, d) not in seen:
                                    if board[c][d] == "O":
                                        stack.append((c,d))
                                        region.append((c,d))
                                        seen.add((c, d))
                            else:
                                valid = False
                    
                    if valid:
                        for elm in region:
                            e, f = elm
                            board[e][f] = "X"

                    


        