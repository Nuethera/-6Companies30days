#
# @lc app=leetcode id=1054 lang=python3
#
# [1054] Distant Barcodes
#

# @lc code=start
class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        fre = [0]*10001
        mc = 0
        for c in barcodes:
            fre[c] += 1
            if fre[c] > fre[mc]:
                mc=c
        
        i, n = 0, len(barcodes)
        ans = [0] * n
        for c in range(10001):
            if c==0:
                c=mc
            for _ in range(fre[c]):
                if i>=n:
                    i=1
                ans[i] = c
                i+=2
            fre[c] = 0
        return ans
# @lc code=end

