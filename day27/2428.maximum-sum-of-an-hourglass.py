#
# @lc app=leetcode id=2428 lang=python3
#
# [2428] Maximum Sum of an Hourglass
#

# @lc code=start
class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        ans = []
        for i in range(1,m-1):
            for j in range(1,n-1):
                s = grid[i-1][j-1]+grid[i-1][j] + grid[i-1][j+1]+grid[i][j]+grid[i+1][j-1]+grid[i+1][j]+grid[i+1][j+1]
                ans.append(s)
        
        return max(ans)
        
# @lc code=end

