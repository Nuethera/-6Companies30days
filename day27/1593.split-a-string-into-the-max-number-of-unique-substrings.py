#
# @lc app=leetcode id=1593 lang=python3
#
# [1593] Split a String Into the Max Number of Unique Substrings
#

# @lc code=start
class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        seen = set()
        def backt(s,seen):
            ans = 0
            if s:
                for i in range(1,len(s)+1):
                    c = s[:i]
                    if c not in seen:
                        seen.add(c)
                        ans = max(ans,1+backt(s[i:],seen))
                        seen.remove(c)
            return ans
        return backt(s, seen)

        
# @lc code=end

