class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows,cols = len(grid), len(grid[0])
        visited = set()
        islands = 0
        def dfs(r,c):
            if not (0 <= r < rows and 0 <= c < cols) or grid[r][c] == "0" or (r,c) in visited:
                return 0
            
            visited.add((r,c))
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    dfs(r,c)
                    islands += 1
        return islands

        