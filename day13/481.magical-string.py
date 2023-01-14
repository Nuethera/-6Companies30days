#
# @lc app=leetcode id=481 lang=python3
#
# [481] Magical String
#

# @lc code=start
class Solution:
    def magicalString(self, n: int) -> int:
        s = ['1','2','2']
        c=1
        i=2
        while len(s) < n:
            if s[-1] == "2":
                c+=int(s[i])
            s += ['2' if s[-1] == '1' else '1']*int(s[i])
            i+=1
        if len(s) == n+1 and s[-1] == '1':
            c-=1

        return c
        
# @lc code=end

