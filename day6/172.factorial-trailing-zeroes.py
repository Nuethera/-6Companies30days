#
# @lc app=leetcode id=172 lang=python3
#
# [172] Factorial Trailing Zeroes
#

# @lc code=start
class Solution:
    def trailingZeroes(self, n: int) -> int:
        return n//5 + n // 25 + n//125 + n//625 + n//3125
        
# @lc code=end

