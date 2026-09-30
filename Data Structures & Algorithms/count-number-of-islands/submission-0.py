# Only 1 and 0, and 1 means land, 0 means water
# grid could be empty
# input: [[str]]
# output: num_of_islands: int, defualt value 0
# Using DFS to solve this problem
# Loop through each node in grid for starting point:
    # if node == '0', we pass it
    # if node == '1', means we found the island, 
    # then we mark the island we found as '2'
    # , we start from the '1''s four directions to found the whole island,
    # then we add one island to our found islands

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        islands = 0

        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            # Check out of bounds
            if r < 0 or r > rows - 1 or c < 0 or c > cols - 1:
                return
            # Check if node is water or visited
            if grid[r][c] == '0':
                return 
            
            grid[r][c] = '0'
            # Go through the surroundings of '1'
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    dfs(i, j)
                    islands += 1
        return islands

