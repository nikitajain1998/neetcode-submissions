class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited= set()
        maxArea = 0

        def dfs(r,c):
            if not(0 <= r < rows and 0 <= c < cols) or grid[r][c] == 0 or (r,c) in visited:
                return 0

            visited.add((r,c))
            area = 1 + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1)
            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    maxArea = max(maxArea, dfs(r,c))
        return maxArea
        