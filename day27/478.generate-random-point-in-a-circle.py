#
# @lc app=leetcode id=478 lang=python3
#
# [478] Generate Random Point in a Circle
#

# @lc code=start
class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.r = radius
        self.center = [x_center,y_center]
        

    def randPoint(self) -> List[float]:
        k = sqrt(uniform(0,1))
        t = uniform(0,2*pi)
        k *= self.r
        t *= 2*math.pi
        return [self.center[0] + k*math.cos(t),self.center[1]+ k*math.sin(t)]



# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()
# @lc code=end

