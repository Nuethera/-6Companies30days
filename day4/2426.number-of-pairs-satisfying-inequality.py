#
# @lc app=leetcode id=2426 lang=python3
#
# [2426] Number of Pairs Satisfying Inequality
#

# @lc code=start
from sortedcontainers import SortedList
class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        o = 0
        n=len(nums1)
        a = [nums1[i] - nums2[i] for i in range(n)]
        an = SortedList(a)
        for i in a:
            an.discard(i)
            l = len(an)
            x = an.bisect_left(i-diff)
            o += l-x
        return o
# @lc code=end

