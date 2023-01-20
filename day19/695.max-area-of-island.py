#
# @lc app=leetcode id=695 lang=python3
#
# [695] Max Area of Island
#

# @lc code=start
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def dfs(i,j):
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == 0: return 0
            grid[i][j] = 0

            return 1+ dfs(i-1,j) + dfs(i+1,j) + dfs(i,j-1) + dfs(i,j+1)

        
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    ans = max(ans, dfs(i, j))

        return ans
        
# @lc code=end

