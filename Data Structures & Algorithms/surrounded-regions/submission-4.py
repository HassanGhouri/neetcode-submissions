class Solution:
    def solve(self, board: List[List[str]]) -> None:

        rows = len(board)
        colums = len(board[0])
        seen = set()

        for i in range(rows):
            for j in range(colums):
                stack = []
                region = []

                if board[i][j] == "O" and (i, j) not in seen:
                    stack.append((i, j))
                    region.append((i, j))
                    captured = True
                    seen.add((i, j))

                    while stack:
                        a, b = stack.pop()
                    
                        adjs = [(a-1,b),(a+1,b),(a,b-1),(a,b+1)]

                        for c, d in adjs:
                            if 0 <= c < rows and 0<= d < colums:
                                if (c, d) not in seen and board[c][d] == "O":
                                    stack.append((c, d))
                                    region.append((c, d))
                                    seen.add((c, d))
                                    
                            
                            else:
                                captured = False
                    
                    if captured:
                        for g, h in region:
                            board[g][h] = "X"

        