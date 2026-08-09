class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        g=[[]for _ in range(n)]
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
        v=set()
        c=0
        def dfs(node):
            if node in v:
                return
            v.add(node)
            for nei in g[node]:
                dfs(nei)
        for i in range(n):
            if i not in v:
                c+=1
                dfs(i)
        return c

        