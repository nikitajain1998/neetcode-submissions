class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        visit = [False] * n

        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)

        def dfs(node):
            for neighbour in adj[node]:
                if not visit[neighbour]:
                     visit[neighbour] = True
                     dfs(neighbour)
        
        res = 0
        for node in range(n):
            if not visit[node]:
                visit[node] = True
                dfs(node)
                res += 1
        return res
        