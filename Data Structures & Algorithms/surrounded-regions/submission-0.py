class Solution:
    def solve(self, board: List[List[str]]) -> None:
        r=len(board)
        c=len(board[0])
        def dfs(i,j):
            if i < 0 or i >= r or j < 0 or j >= c:
                return
            if board[i][j]!="O":
                return
            board[i][j]="S"
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)

        for i in range(r):
            dfs(i,0)
            dfs(i,c-1)
        for j in range(c):
            dfs(0,j)
            dfs(r-1,j)
        for i in range(r):
            for j in range(c):
                if board[i][j]=="O":
                    board[i][j]="X"
                elif board[i][j] == "S":
                        board[i][j] = "O"
    