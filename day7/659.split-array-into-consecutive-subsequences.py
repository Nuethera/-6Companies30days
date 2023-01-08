#
# @lc app=leetcode id=659 lang=python3
#
# [659] Split Array into Consecutive Subsequences
#

# @lc code=start
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        avail = defaultdict(int)
        vacan = defaultdict(int)
        for i in nums:
            avail[i] += 1

        for i in nums:
            if avail[i] <= 0:
                continue
            elif vacan[i]>0:
                avail[i] -= 1
                vacan[i] -= 1
                vacan[i+1] += 1

            elif avail[i] > 0 and avail[i+1] > 0 and avail[i+2] > 0:
                avail[i] -= 1
                avail[i+1] -= 1
                avail[i+2] -= 1
                vacan[i+3] += 1
            else:
                return False
                

        return True
        
# @lc code=end

