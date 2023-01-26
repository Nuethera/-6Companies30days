#
# @lc app=leetcode id=1314 lang=python3
#
# [1314] Matrix Block Sum
#

# @lc code=start
class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        pre = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                pre[i][j] = mat[i-1][j-1] + pre[i][j-1] +pre[i-1][j] - pre[i-1][j-1]
        
        ans = [[0] * n for _ in range(m)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                ei = min(i+k,m)
                ej = min(j+k,n)
                si,sj = max(i-k,1), max(j-k,1)
                ans[i-1][j-1] = pre[ei][ej] - pre[si-1][ej] - pre[ei][sj-1] + pre[si-1][sj-1]
        
        return ans
        
# @lc code=end

