#
# @lc app=leetcode id=216 lang=python3
#
# [216] Combination Sum III
#

# @lc code=start
class Solution:
    def bcktrck(self,t,k,n,num,a):
        if k==0:
            if sum(t) == n:
                a.append(t.copy())
            return
            
        if num>9:
            return
        t.append(num)
        self.bcktrck(t,k-1,n,num+1,a)
        t.pop()
        self.bcktrck(t,k,n,num+1,a)


    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        a = []
        self.bcktrck([],k,n,1,a)
        return a
        
        
# @lc code=end

