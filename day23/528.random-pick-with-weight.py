#
# @lc app=leetcode id=528 lang=python3
#
# [528] Random Pick with Weight
#

# @lc code=start
class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        s = sum(self.w)
        for i in range(len(self.w)):
            self.w[i] = self.w[i] / s
        for i in range(1,len(self.w)):
            self.w[i] += self.w[i-1]
        

    def pickIndex(self) -> int:
        N = random.uniform(0,1)
        i=0
        j=len(self.w)
        while i <= j:
            m = (i+j)//2
            if self.w[m]>N:
                j=m-1
            elif self.w[m]<N:
                i=m+1
            else:
                return m


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
# @lc code=end

