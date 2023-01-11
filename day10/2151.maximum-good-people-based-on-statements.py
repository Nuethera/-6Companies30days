#
# @lc app=leetcode id=2151 lang=python3
#
# [2151] Maximum Good People Based on Statements
#

# @lc code=start
class Solution:
    def maximumGood(self, statements: List[List[int]]) -> int:
        self.ans = 0
        n = len(statements)
        def valid(curr):
            for i in range(n):
                if curr[i]:
                    for j in range(n):
                        if statements[i][j]!=2 and statements[i][j] != curr[j]:
                            return False
            
            return True
        
        def back(arr, i, cnt):
            if i==n:
                if valid(arr):
                    self.ans = max(self.ans,cnt)
                return
            arr.append(0)
            back(arr,i+1,cnt)
            arr[-1] = 1
            back(arr,i+1,cnt+1)
            arr.pop()
        
        back([],0,0)

        return self.ans
# @lc code=end

