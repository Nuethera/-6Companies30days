#
# @lc app=leetcode id=1461 lang=python3
#
# [1461] Check If a String Contains All Binary Codes of Size K
#

# @lc code=start
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        st = set()
        for i in range(k, len(s) + 1):
            st.add(s[i - k : i])
            if len(st) == 1 << k:
                break
        return len(st) == 1 << k
        
# @lc code=end

