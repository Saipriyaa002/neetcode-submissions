class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        r=len(grid)
        c=len(grid[0])
        t=0
        def dfs(i,j):
            if i<0 or i>=r or j<0 or j>=c:
                return
            if grid[i][j]=="0":
                return
            grid[i][j]="0"
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
        for i in range(r):
            for j in range(c):
                if grid[i][j]=="1":
                    t+=1
                    dfs(i,j)
        return t