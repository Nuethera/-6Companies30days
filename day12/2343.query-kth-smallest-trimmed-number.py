#
# @lc app=leetcode id=2343 lang=python3
#
# [2343] Query Kth Smallest Trimmed Number
#

# @lc code=start
class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        ind = list(range(len(queries)))
        ind.sort(reverse=True, key=lambda i:queries[i][1])
        ans = [-1] * len(queries)
        for i in ind:
            q = queries[i]
            t = SortedList()
            f = [(int(nums[k][-q[1]:]),k) for k in range(len(nums)) ]
            f.sort(key=lambda x:x[0])
            ans[i] = f[q[0]-1][1]
                
        
        return ans
        
# @lc code=end

