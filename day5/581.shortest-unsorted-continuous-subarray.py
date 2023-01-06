#
# @lc app=leetcode id=581 lang=python3
#
# [581] Shortest Unsorted Continuous Subarray
#

# @lc code=start
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        i=0
        while i<len(nums)-1 and nums[i]<=nums[i+1]:
            i+=1
        
        j=len(nums)-1
        while j>0 and nums[j]>=nums[j-1]:
            j-=1
        if i>j:
            return 0
        m,M = min(nums[i:j+1]),max(nums[i:j+1])

        s,e=0,len(nums)-1
        while s<=i and nums[s]<=m:
            s+=1
        while e>j and nums[e]>=M:
            e-=1

        return e-s+1
            
        
# @lc code=end

