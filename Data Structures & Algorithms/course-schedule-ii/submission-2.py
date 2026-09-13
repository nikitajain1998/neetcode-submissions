class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for i in range(numCourses)]
        indegree = [0] * numCourses

        for i,j in prerequisites:
            adj[j].append(i)
            indegree[i] += 1
        
        q = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        order = []
        while q:
            node = q.popleft()
            order.append(node)

            for n in adj[node]:
                indegree[n] -= 1
                if indegree[n] == 0:
                    q.append(n)

        return order if len(order) == numCourses else []