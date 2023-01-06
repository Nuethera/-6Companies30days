#
# @lc app=leetcode id=1358 lang=python3
#
# [1358] Number of Substrings Containing All Three Characters
#

# @lc code=start
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        i,j=0,0
        a=0
        d = {'a':0,'c':0,'b':0}
        while j < len(s):
            d[s[j]] += 1
            while d['a'] > 0 and d['b'] > 0 and d['c'] > 0 and i <= j:
                d[s[i]] -= 1
                i += 1
                a += len(s) - j

            j+=1
        
        return a
        
# @lc code=end

