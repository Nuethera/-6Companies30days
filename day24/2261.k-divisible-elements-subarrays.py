#
# @lc app=leetcode id=2261 lang=python3
#
# [2261] K Divisible Elements Subarrays
#

# @lc code=start
class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        s = set()
        for i in range(len(nums)):
            t= ""
            c=0
            for j in range(i,len(nums)):
                if nums[j] % p==0:
                    c+=1
                if c > k:
                    break                
                t+=str(nums[j])+','
                s.add(t)

        return len(s)
        
# @lc code=end

