#
# @lc app=leetcode id=1227 lang=python3
#
# [1227] Airplane Seat Assignment Probability
#

# @lc code=start
class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        if n==1:
            return 1
        else: return 0.5
        
# @lc code=end

