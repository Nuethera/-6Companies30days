#
# @lc app=leetcode id=1814 lang=python3
#
# [1814] Count Nice Pairs in an Array
#

# @lc code=start
class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        fs = Counter(i - int(str(i)[::-1]) for i in nums)
        return sum(f * (f - 1) // 2 for f in fs.values()) % 1000000007
        
# @lc code=end

