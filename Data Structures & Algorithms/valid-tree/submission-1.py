class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for i in range(n)]

        for i ,j in edges:
            adj[i].append(j)
            adj[j].append(i)
        
        visit =set()
        def dfs(i, parent):
            if i in visit:
                return False
            visit.add(i)
            for j in adj[i]:
                if j ==parent:
                    continue
                if not dfs(j,i):
                    return False
            return True
        
        return dfs(0, -1) and len(visit) == n
        