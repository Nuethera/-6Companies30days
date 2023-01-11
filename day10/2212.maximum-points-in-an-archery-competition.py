#
# @lc app=leetcode id=2212 lang=python3
#
# [2212] Maximum Points in an Archery Competition
#

# @lc code=start
class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        self.score = 0
        self.barr = None

        def backtracking(k,remArrows, sc, bArr):
            if k==12:
                if sc > self.score:
                    self.score = sc
                    self.barr = bArr[:]
                return
            
            backtracking(k+1,remArrows,sc,bArr)
            if remArrows >= aliceArrows[k] + 1:
                o = bArr[k]
                bArr[k] = aliceArrows[k] + 1

                backtracking(k+1,remArrows - aliceArrows[k] - 1,sc+k,bArr)
                bArr[k] = o
            
        backtracking(0,numArrows,0,[0]*12)

        self.barr[0] += numArrows - sum(self.barr)
        return self.barr
        
        
# @lc code=end

