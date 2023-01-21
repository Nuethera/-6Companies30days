#
# @lc app=leetcode id=837 lang=python3
#
# [837] New 21 Game
#

# @lc code=start
class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or n >= k + maxPts: return 1
        dp = [1.0] + [0.0] * n
        Wsum = 1.0
        for i in range(1, n + 1):
            dp[i] = Wsum / maxPts
            if i < k: Wsum += dp[i]
            if i - maxPts >= 0: Wsum -= dp[i - maxPts]
        return sum(dp[k:])
        
# @lc code=end

