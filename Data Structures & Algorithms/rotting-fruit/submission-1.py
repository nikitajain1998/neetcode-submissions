class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        time, fresh = 0, 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append([r,c])
        
        def addNeighbours(r,c):
            nonlocal fresh
            if not(0 <= r < rows and 0 <= c < cols) or grid[r][c] == 2 or grid[r][c] == 0:
                return
            q.append([r,c])
            grid[r][c] = 2
            fresh -= 1
        
        while q and fresh > 0:
            for _ in range(len(q)):
                r,c = q.popleft()
                addNeighbours(r+1,c)
                addNeighbours(r-1,c)
                addNeighbours(r,c+1)
                addNeighbours(r,c-1)
            time += 1
        
        return time if fresh == 0 else -1
        