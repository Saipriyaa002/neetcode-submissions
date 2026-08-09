class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)
        g=[[]for _ in range(n+1)]
        def dfs(node,t,v):
            if node==t:
                return True
            v.add(node)
            for nei in g[node]:
                if nei not in v:
                    if dfs(nei,t,v):
                        return True
            return False
        for a,b in edges:
            v=set()
            if dfs(a,b,v):
                return [a,b]
            g[a].append(b)
            g[b].append(a)
        return []