#
# @lc app=leetcode id=396 lang=python3
#
# [396] Rotate Function
#

# @lc code=start
class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        c = sum(i*j for i,j in enumerate(nums))
        f=c
        n = len(nums)
        s = sum(nums)
        while nums:
            c += s - nums.pop()*n
            f=max(f,c)
            
        return f
        
# @lc code=end

