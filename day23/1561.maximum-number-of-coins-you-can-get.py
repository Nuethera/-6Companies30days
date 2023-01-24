#
# @lc app=leetcode id=1561 lang=python3
#
# [1561] Maximum Number of Coins You Can Get
#

# @lc code=start
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        n = len(piles) // 3
        i = 1
        ans = 0
        while i<2*n:
            ans += piles[i]
            i+=2
        return ans

        
# @lc code=end

