#
# @lc app=leetcode id=600 lang=python3
#
# [600] Non-negative Integers without Consecutive Ones
#

# @lc code=start
class Solution:
    def findIntegers(self, n: int) -> int:
        if n<=2:
            return n+1
        f = [1, 2]
        for i in range(2, 30):
            f.append(f[-1]+f[-2])

        ans, last_seen = 0, 0
        for i in reversed(range(30)):
            if (1 << i) & n: 
                ans += f[i]
                if last_seen: 
                    ans -= 1
                    break
                last_seen = 1
            else:
                last_seen = 0
        return ans+1
# @lc code=end

