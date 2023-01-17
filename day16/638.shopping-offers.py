#
# @lc app=leetcode id=638 lang=python3
#
# [638] Shopping Offers
#

# @lc code=start
class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        d = {}
        def dfs(cur):
            val = sum([cur[i]*price[i] for i in range(len(needs))])
            for spec in special:
                t = [cur[j] - spec[j] for j in range(len(needs))]
                if min(t) >= 0:
                    if tuple(t) in d:
                        val = min(val, d[tuple(t)]+spec[-1])
                    else:
                        val = min(val,  dfs(t)+spec[-1])
            d[tuple(cur)] = val
            return val
        
        return dfs(needs)
        
# @lc code=end

