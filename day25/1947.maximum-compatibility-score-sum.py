#
# @lc app=leetcode id=1947 lang=python3
#
# [1947] Maximum Compatibility Score Sum
#

# @lc code=start
class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        m=len(students)
        n=len(students[0])
        self.ans = 0

        def findS(s,m):
            c = 0
            for i in range(n):
                if s[i] == m[i]:
                    c+=1
            return c




        def backt(i,mask,score):
            if i == m:
                self.ans = max(self.ans, score)
                return 
            
            for j in range(m):
                if mask & (1<<j) == 0:
                    backt(i+1, mask | (1<<j), score+findS(students[i], mentors[j]))
            

        backt(0,0,0)
        return self.ans

        
# @lc code=end

