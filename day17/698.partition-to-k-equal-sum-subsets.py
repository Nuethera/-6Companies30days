#
# @lc app=leetcode id=698 lang=python3
#
# [698] Partition to K Equal Sum Subsets
#

# @lc code=start
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        ssum = sum(nums)
        if ssum % k != 0:
            return False
        target = sum(nums) // k
        if any(num > target for num in nums): return False
        nums.sort()
        while target in nums:
            nums.remove(target)
            k -= 1

        seen = [False] * len(nums)
        @cache
        def bp(seen, i, total, k):
            if k == 0:                      return True
            if k == 1 and total == 0:       return True
            if i == len(nums) or total < 0: return False

            #Reset when we successfully find a partition sum == target
            if total == 0: 
                total = target
                k -= 1
                i = 0

            seen = list(seen)
            if seen[i] == False:
                seen[i] = True
                if bp(tuple(seen), i + 1, total - nums[i], k): return True
                seen[i] = False

            return bp(tuple(seen), i + 1, total, k) 

        return bp(tuple(seen), 0, target, k)
        
# @lc code=end

