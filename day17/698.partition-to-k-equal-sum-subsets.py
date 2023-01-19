#
# @lc app=leetcode id=698 lang=python3
#
# [698] Partition to K Equal Sum Subsets
#

# @lc code=start
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)

        if total % k:
            return False

        target = total // k
        subSet = [0] * k
        nums.sort(reverse = True)
        def recurse(i):
            if i==len(nums):
                return True
            
            for j in range(k):
                if subSet[j] + nums[i] <= target:
                    subSet[j] += nums[i]

                    if recurse(i+1):
                        return True
                    
                    subSet[j] -= nums[i]
                    if subSet[j] == 0:
                        break
            
            return False
        
        return recurse(0)
        
        
# @lc code=end

