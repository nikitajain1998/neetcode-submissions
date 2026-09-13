class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        rows,cols = len(grid), len(grid[0])
        dist = 0
        visited = set()
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    visited.add((r,c))
                    q.append((r,c))

        def addNeighbour(r,c):
            if not (0 <= r< rows and 0<= c < cols) or grid[r][c] ==-1 or (r,c) in visited:
                return
            q.append((r,c))
            visited.add((r,c))


        while q:
            for i in range(len(q)):
                r, c =q.popleft()
                grid[r][c] = dist
                addNeighbour(r+1, c)
                addNeighbour(r-1, c)
                addNeighbour(r, c+1)
                addNeighbour(r, c-1)
            dist += 1
        
    






        