class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = [[] for _ in range(n+1)]
        for i,j in edges:
            adj[i].append(j)
            adj[j].append(i)
        
        visit = [False] * (n+1)

        cycle =set()
        cycleStart = -1
        def dfs(node, parent):
            nonlocal cycleStart
            if visit[node]:
                cycleStart = node
                return True
            visit[node] = True
            for nei in adj[node]:
                if nei == parent:
                    continue
                if dfs(nei, node):
                    if cycleStart != -1:
                        cycle.add(node)
                    if node == cycleStart:
                        cycleStart = -1
                    return True
            
        dfs(1, -1)

        for i,j in reversed(edges):
            if i in cycle and j in cycle:
                return [i,j]
        return []

        