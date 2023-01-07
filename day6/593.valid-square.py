#
# @lc app=leetcode id=593 lang=python3
#
# [593] Valid Square
#

# @lc code=start
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        sides = [0] * 6
        def dist(a,b):
            return int((a[0]-b[0])**2 + (a[1]-b[1])**2)
        
        sides[0] = dist(p1,p2)
        sides[1] = dist(p1,p3)
        sides[2] = dist(p1,p4)
        sides[3] = dist(p2,p3)
        sides[4] = dist(p2,p4)
        sides[5] = dist(p3,p4)

        side = min(sides)
        s,d=0,0
        for i in sides:
            if i == side:
                s+=1
            elif i == side*2:
                d+=1
        return s==4 and d==2
# @lc code=end

