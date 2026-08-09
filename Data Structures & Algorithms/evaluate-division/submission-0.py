class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = {}

        # Build graph
        for account in accounts:
            first = account[1]

            if first not in graph:
                graph[first] = []

            for email in account[2:]:
                graph.setdefault(email, [])
                graph[first].append(email)
                graph[email].append(first)

        visited = set()
        ans = []

        for account in accounts:
            name = account[0]
            first = account[1]

            if first in visited:
                continue

            emails = []

            def dfs(email):
                if email in visited:
                    return

                visited.add(email)
                emails.append(email)

                for nei in graph[email]:
                    dfs(nei)

            dfs(first)

            emails.sort()
            ans.append([name] + emails)

        return ans