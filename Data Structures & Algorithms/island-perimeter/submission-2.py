class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        r=len(grid)
        c=len(grid[0])
        p=0
        for i in range(r):
            for j in range(c):
                if grid[i][j]==1:
                    p+=4
                    if i+1<r and grid[i+1][j]==1:
                        p-=2
                    if j+1<c and grid[i][j+1]==1:
                        p-=2
        return p