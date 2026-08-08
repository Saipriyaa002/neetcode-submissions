class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]

        for a, b in prerequisites:
            graph[b].append(a)

        visited = set()
        path = set()

        def dfs(course):
            if course in path:
                return False

            if course in visited:
                return True

            path.add(course)

            for next_course in graph[course]:
                if not dfs(next_course):
                    return False

            path.remove(course)
            visited.add(course)

            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True