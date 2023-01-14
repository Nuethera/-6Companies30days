#
# @lc app=leetcode id=440 lang=python3
#
# [440] K-th Smallest in Lexicographical Order
#

# @lc code=start
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        res = 1
        k-=1
        while k>0:
            i = [res,res+1]
            c = 0
            while i[0]<=n:
                c += min(n+1, i[1]) - i[0]
                i[0] *= 10
                i[1] *= 10
            
            if k>=c:
                res += 1
                k-=c
            else:
                res*=10
                k-=1
            
        return res
        
# @lc code=end

