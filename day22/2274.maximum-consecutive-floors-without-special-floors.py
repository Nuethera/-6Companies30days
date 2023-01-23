#
# @lc app=leetcode id=2274 lang=python3
#
# [2274] Maximum Consecutive Floors Without Special Floors
#

# @lc code=start
class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        if top - bottom + 1 == len(special):
            return 0
        special.sort()
        res = special[0] - bottom        
        for i in range(1, len(special)):
            res = max(res, special[i] - special[i - 1] - 1)
            
        return max(res, top - special[-1])
        
# @lc code=end

