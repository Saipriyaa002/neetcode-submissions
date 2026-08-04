class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        a=[]
        def dfs(s,p):
            if len(p)==k:
                a.append(p[:])
                return

            for i in range(s,n+1):
                p.append(i)
                dfs(i+1,p)
                p.pop()
        dfs(1,[])
        return a