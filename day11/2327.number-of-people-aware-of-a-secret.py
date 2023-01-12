#
# @lc app=leetcode id=2327 lang=python3
#
# [2327] Number of People Aware of a Secret
#

# @lc code=start
class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        h = [1] + [0]*(n-1)
        a = 0
        for i in range(1,n):
            a = (a + h[i-delay] - h[i-forget]) % 1000000007
            h[i] = a
        return sum(h[-forget:]) % 1000000007
        
# @lc code=end

