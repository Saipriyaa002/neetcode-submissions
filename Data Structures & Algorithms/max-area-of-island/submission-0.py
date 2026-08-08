class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        r=len(grid)
        c=len(grid[0])
        a=0
        def dfs(i,j):
            if i<0 or i>=r or j<0 or j>=c:
                return 0
            if grid[i][j]==0:
                return 0
            grid[i][j]=0
            return 1+dfs(i+1,j)+dfs(i-1,j)+dfs(i,j+1)+dfs(i,j-1)
        for i in range(r):
            for j in range(c):
                if grid[i][j]==1:
                    b=dfs(i,j)
                    a=max(a,b)
        return a