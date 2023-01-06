#
# @lc app=leetcode id=1392 lang=python3
#
# [1392] Longest Happy Prefix
#

# @lc code=start
class Solution:
    def longestPrefix(self, s: str) -> str:
        if len(s) == 1:
            return ""
        base, MOD = 29, 10**9 + 7
        lookup = []
        seed, n = 1, len(s)
        for i in range(n):
            lookup.append(seed)
            seed *= base
            seed %= MOD
        res,l,r = 0,0,0
        for i in range(n-1):
            l = (l*base + ord(s[i]))% MOD
            r = (r+(lookup[i]*ord(s[~i]) ))% MOD
            if l==r:
                res = i+1
        return s[:res]
        
# @lc code=end

