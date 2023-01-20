#
# @lc app=leetcode id=1823 lang=python3
#
# [1823] Find the Winner of the Circular Game
#

# @lc code=start
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        f = list(range(n))
        i=0
        while len(f)>1:
            i = (i+k-1) % len(f)
            f.pop(i)
            
        return f[0] + 1
        
# @lc code=end

