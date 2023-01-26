#
# @lc app=leetcode id=2396 lang=python3
#
# [2396] Strictly Palindromic Number
#

# @lc code=start
class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def ispalin(s):
            a,b = 0,len(s)-1
            while a<b:
                if s[a] != s[b]:
                    return False
                a+=1
                b-=1
            return True
        
        for i in range(2,n-1):
            a = ""
            t = n
            while t:
                a+= str(t%i)
                t = t//i
            if not ispalin(a):
                return False
        
        return True

# @lc code=end

