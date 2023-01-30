#
# @lc app=leetcode id=2400 lang=python3
#
# [2400] Number of Ways to Reach a Position After Exactly k Steps
#

# @lc code=start
class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        MOD = 1000000007

        diff = abs(startPos-endPos)
        if diff > k or diff%2 != k%2:
            return 0

        r = (diff+k)//2
        return math.comb(k,r)%MOD
        
# @lc code=end

