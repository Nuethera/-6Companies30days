#
# @lc app=leetcode id=1254 lang=python3
#
# [1254] Number of Closed Islands
#

# @lc code=start
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        if grid[i][j] == -1 or grid[i][j] == 1:
            return True
        if i in [0,m-1] or j in [0,n-1]:
            return False        
        grid[i][j] = -1
        a = self.isClosed(grid,i,j-1,m,n)
        b = self.isClosed(grid,i,j+1,m,n)
        c = self.isClosed(grid,i+1,j,m,n)
        d = self.isClosed(grid,i-1,j,m,n)
        
        return a and b and c and d
    
    def closedIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        m = len(grid)
        n = len(grid[0])
        
        for i in range(1,m-1):
            for j in range(1,n-1):
                if grid[i][j] == 0:
                   if self.isClosed(grid, i, j,m,n):
                       ans+=1

        return ans
        
# @lc code=end

