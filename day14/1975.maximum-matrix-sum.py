#
# @lc app=leetcode id=1975 lang=python3
#
# [1975] Maximum Matrix Sum
#

# @lc code=start
class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = float('inf')
        c = s = 0
        
        for i in range(n):
            for j in range(n):
                m = min(m, abs(matrix[i][j]))
                if matrix[i][j] < 0:
                    c += 1
                s += abs(matrix[i][j])

        if c%2==0:
            return s
        return s - (2*m)

        
# @lc code=end

