#
# @lc app=leetcode id=2456 lang=python3
#
# [2456] Most Popular Video Creator
#

# @lc code=start
class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        tv = defaultdict(int)
        vids = defaultdict(list)
        
        for c, i, v in zip(creators,ids,views):
            tv[c]+=v
            vids[c].append((-v,i))
        
        m = max(tv.values())

        ans = [[c,min(v)[1]] for c,v in vids.items() if tv[c] == m]

        return ans
        
# @lc code=end

