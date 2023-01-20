#
# @lc app=leetcode id=791 lang=python3
#
# [791] Custom Sort String
#

# @lc code=start
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        h = defaultdict(int)
        for i in s:
            h[i]+=1
        a = ""
        for i in order:
            a += i*h[i]
            h[i] = 0
        
        for i,f in h.items():
            if f>0:
                a += i*f
            
        return a
        
# @lc code=end

