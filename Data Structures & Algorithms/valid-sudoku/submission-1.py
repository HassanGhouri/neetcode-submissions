class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(len(board)):
            seen = set()
            for j in range(len(board)):
                print(print(i, j, board[i][j]), seen)
                if board[i][j] in seen and board[i][j] != ".":
                    return False
                
                else:
                    seen.add(board[i][j])
        
        for i in range(len(board)):
            seen = set()
            for j in range(len(board)):
                if board[j][i] in seen and board[j][i] != ".":
                    return False
                
                else:
                    seen.add(board[j][i])
        
        row_offsets = [0, 3, 6]
        colum_offsets = [0, 3, 6]

        for row_offset in row_offsets:
            for colum_offset in colum_offsets:
                seen = set()

                for i in range(row_offset, row_offset + 3):
                    for j in range(colum_offset, colum_offset + 3):
                        if board[i][j] in seen and board[i][j] != ".":
                            return False
                    
                        else:
                            seen.add(board[i][j])
        
        return True

