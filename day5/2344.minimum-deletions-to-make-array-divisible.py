#
# @lc app=leetcode id=2344 lang=python3
#
# [2344] Minimum Deletions to Make Array Divisible
#

# @lc code=start
class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        gc=0
        for i in numsDivide:
            gc=int(math.gcd(gc,i))
        nums.sort()
        i=0
        while i < len(nums):
            if gc % nums[i] == 0:
                return i
            i+=1
        return -1
# @lc code=end

